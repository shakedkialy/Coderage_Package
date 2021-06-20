import os
import xml.etree.ElementTree as et
from datetime import datetime, timezone
import re

class Parser:
    """
    this class implements a parser which parses the test and coverage results.
    """

    def __init__(self, db, directory):
        """
        init a parser object
        :param db: the DB which will hold the parsed information
        :param directory: the directory of the result files that needs to be parsed.
        """
        self.__db = db
        self.__directory = directory
        self.__runId = self.__db.get_last_run_id() + 1
        self.parse_pytest()
        self.parseCoverage()
        self.parseAnnotate()

    def parse_pytest(self):
        """
        parses the results of the pytest run and inserts to the relevant tables in the DB.
        """
        file_path = os.path.join(self.__directory, "tests.xml")
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
        """
        parses the results of the coverage run and inserts to the relevant tables in the DB.
        (results of the coverage run  = how many lines are covered)
        """
        file_path = os.path.join(self.__directory, "coverage.xml")
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
        """
        iterates all the annotate files created and parses each one using parseAnnotateFile function.
        """
        if os.path.isdir(self.__directory):
            for filename in os.listdir(os.path.join(self.__directory, "annotate")):
                if filename.endswith(",cover"):
                    self.parseAnnotateFile(os.path.join(self.__directory, "annotate", filename))
        if os.path.isfile(self.__directory):
            self.parseAnnotateFile(self.__directory)

    def parseAnnotateFile(self, file_path):
        """
        parses the results of the annotate run and inserts to the relevant tables in the DB.
        (results of the annotate run  = which functions are being run and which aren't)
        """
        function_details_rows = []
        file_name = os.path.basename(file_path)
        file_name = file_name[:file_name.index(',')]
        file_name = file_name.replace('_', '/')
        with open(file_path, 'r') as file:
            functions = re.split('(\s)+def', file.read())
            for function in functions[1:]:
                function_name = function.split('\n')[0]
                try:
                    function_name = function_name[:function_name.index("(")]
                except:
                    continue
                is_tested = 0
                if '>' in function:
                    is_tested = 1
                function_details_rows.append((self.__runId, file_name, function_name, is_tested))

        self.__db.insert_functions_details(function_details_rows)

    def get_run_id(self):
        """
        :return: the current runId
        """
        return self.__runId
