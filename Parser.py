import os
import xml.etree.ElementTree as et
from datetime import datetime, timezone


class Parser:

    def __init__(self, db, directory):
        self.__db = db
        self.__directory = directory
        self.__runId = self.__db.get_last_run_id() + 1
        self.parse_pytest()
        self.parseCoverage()
        self.parseAnnotate()

    def parse_pytest(self):
        file_path = self.__directory + "/tests.xml"
        tree = et.parse(file_path)
        root = tree.getroot()
        test_rows = []
        summary_rows = []

        # TODO change timestamp to same string format in all tables
        for element in root:
            summary_rows.append((self.__runId, int(element.attrib["errors"]),
                                 int(element.attrib["tests"]) - int(element.attrib["failures"]),
                                 int(element.attrib["failures"]),
                                 int(element.attrib["skipped"]),
                                 float(element.attrib["time"]),
                                 datetime.strptime(element.attrib["timestamp"], '%Y-%m-%dT%H:%M:%S.%f').strftime(
                                     '%Y-%m-%d %H:%M:%S')))
            for child in element:
                if not len(child):
                    test_rows.append((self.__runId, child.attrib["classname"], child.attrib["name"], 1, None, float(child.attrib["time"])))
                else:
                    for grandchild in child:
                        test_rows.append((self.__runId, child.attrib["classname"], child.attrib["name"], 0, grandchild.text, float(child.attrib["time"])))

        self.__db.insert_tests_details(test_rows)
        self.__db.insert_run_summary(summary_rows)


    def parseCoverage(self):
        file_path = self.__directory + "/coverage.xml"
        tree = et.parse(file_path)
        root = tree.getroot()
        coverage_rows = []
        sum_rows = []

        unix = datetime.utcfromtimestamp(int(root.attrib["timestamp"][:10]))
        timestamp = unix.replace(tzinfo=timezone.utc).astimezone(tz=None).strftime('%Y-%m-%d %H:%M:%S')
        sum_rows.append((self.__runId, float(root.attrib["line-rate"]),
                         int(root.attrib["lines-valid"]), timestamp))
        for element in root:
            if element.tag == 'packages':
                for package in element:
                    for classes in package:
                        for testClass in classes:
                            coverage_rows.append((self.__runId,
                                                   float(testClass.attrib["line-rate"]), package.attrib["name"], testClass.attrib["filename"], testClass.attrib["name"]))

        self.__db.insert_coverage(coverage_rows)
        self.__db.insert_coverage_summary(sum_rows)

    def parseAnnotate(self):
        if os.path.isdir(self.__directory):
            for filename in os.listdir(self.__directory):
                if filename.endswith(",cover"):
                    self.parseAnnotateFile(self.__directory + "/" + filename)
        if os.path.isfile(self.__directory):
            self.parseAnnotateFile(self.__directory)

    def parseAnnotateFile(self, file_path):
        function_details_rows = []
        file_name = file_path.split('\\')[-1]
        file_name = file_name[:file_name.index(',')]
        with open(file_path, 'r') as file:
            functions = file.read().split('> def')
            for function in functions[1:]:
                function_name = function.split('\n')[0]
                function_name = function_name[:function_name.index("(")]
                is_tested = 0
                if '>' in function:
                    is_tested = 1
                function_details_rows.append((self.__runId, file_name, function_name, is_tested))

        self.__db.insert_functions_details(function_details_rows)

    def get_run_id(self):
        return self.__runId
