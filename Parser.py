import os
import xml.etree.ElementTree as et


class Parser:

    def __init__(self, db, directory):
        self.db = db
        self.directory = directory
        self.passTests = {}
        self.failTests = {}
        self.cover = {}
        self.uncover = {}
        self.runId = self.db.get_last_run_id()
        self.runId = 1 if self.runId is None else self.runId + 1
        self.parse_pytest()
        self.parseCoverage()
        self.parseAnnotate()

    def parse_pytest(self):
        file_path = self.directory + "/tests.xml"
        tree = et.parse(file_path)
        root = tree.getroot()
        test_rows = []
        summary_rows = []

        # TODO change timestamp to same string format in all tables
        for element in root:
            summary_rows.append((self.runId, int(element.attrib["errors"]),
                                 int(element.attrib["tests"]) - int(element.attrib["failures"]),
                                 int(element.attrib["failures"]),
                                 int(element.attrib["skipped"]),
                                 float(element.attrib["time"]),
                                 element.attrib["timestamp"]))
            for child in element:
                if not len(child):
                    self.passTests[child.attrib["name"]] = child.attrib["classname"]
                    test_rows.append((self.runId, child.attrib["classname"], child.attrib["name"], 1, None, float(child.attrib["time"])))
                else:
                    for grandchild in child:
                        self.failTests[child.attrib["name"]] = grandchild.text
                        test_rows.append((self.runId, child.attrib["classname"], child.attrib["name"], 0, grandchild.text, float(child.attrib["time"])))

        self.db.insert_tests_details(test_rows)
        self.db.insert_run_summary(summary_rows)

        # print("----------- Passed / Failed -----------")
        # print(test_rows)
        # print(summary_rows)

    def parseCoverage(self):
        file_path = self.directory + "/coverage.xml"
        tree = et.parse(file_path)
        root = tree.getroot()
        coverage_rows = []
        sum_rows = []

        sum_rows.append((self.runId, float(root.attrib["line-rate"]),
                         int(root.attrib["lines-valid"]), root.attrib["timestamp"]))
        for element in root:
            if element.tag == 'packages':
                for package in element:
                    for classes in package:
                        for testClass in classes:
                            coverage_rows.append((self.runId,
                                                  float(testClass.attrib["line-rate"]), package.attrib["name"], testClass.attrib["filename"], testClass.attrib["name"]))
                            for classContest in testClass:
                                if classContest.tag == 'lines':
                                    for line in classContest:
                                        className = testClass.attrib['name']
                                        lineNumber = line.attrib['number']
                                        if line.attrib['hits'] == '1':
                                            try:
                                                self.cover[className].add(lineNumber)
                                            except KeyError:
                                                self.cover[className] = {lineNumber}
                                        else:
                                            try:
                                                self.uncover[className].add(
                                                    lineNumber)
                                            except KeyError:
                                                self.uncover[className] = {
                                                    lineNumber}

        self.db.insert_coverage(coverage_rows)
        self.db.insert_coverage_summary(sum_rows)

        # print("----------- Coverage -----------")
        # print(sum_rows)
        # print(coverage_rows)

    def parseAnnotate(self):
        dir_path = self.directory + "/annotate"
        for filename in os.listdir(dir_path):
            if filename.endswith(",cover"):
                self.parseAnnotateFile(dir_path + "/" + filename)

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
                function_details_rows.append((self.runId, file_name, function_name, is_tested))

        self.db.insert_functions_details(function_details_rows)
        # print(function_details_rows)
