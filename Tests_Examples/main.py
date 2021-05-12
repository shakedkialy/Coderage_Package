import os
import xml.etree.ElementTree as et

def parsePytest(file_path):
    tree = et.parse(file_path)
    root = tree.getroot()

    passTests = {}
    failTests = {}
    test_rows = []
    summary_rows = []
    runId = 0

    # TODO change timestamp to same string format in all tables
    for element in root:
        summary_rows.append([runId, int(element.attrib["errors"]), int(element.attrib["tests"]) - int(element.attrib["failures"]), int(element.attrib["failures"]), int(element.attrib["skipped"]), float(element.attrib["time"]), element.attrib["timestamp"]])
        for child in element:
            if not len(child):
                passTests[child.attrib["name"]] = child.attrib["classname"]
                test_rows.append([runId, child.attrib["classname"], child.attrib["name"], 1, None, float(child.attrib["time"])])
            else:
                for grandchild in child:
                    failTests[child.attrib["name"]] = grandchild.text
                    test_rows.append(
                        [runId, child.attrib["classname"], child.attrib["name"], 0, grandchild.text, float(child.attrib["time"])])

    # call insert function

    print("----------- Passed / Failed -----------")
    print(passTests)
    print(failTests)
    print(test_rows)
    print(summary_rows)

def parseCoverage(file_path):
    tree = et.parse(file_path)
    root = tree.getroot()
    runId = 0
    coverarge_rows = []
    sum_rows = []

    cover = {}
    uncover = {}
    sum_rows.append([runId, float(root.attrib["line-rate"]), int(root.attrib["lines-valid"]), root.attrib["timestamp"]])
    for element in root:
        if element.tag == 'packages':
            for package in element:
                for classes in package:
                    for testClass in classes:
                        coverarge_rows.append([runId, float(testClass.attrib["line-rate"]), package.attrib["name"], testClass.attrib["filename"], testClass.attrib["name"]])
                        for classContest in testClass:
                            if classContest.tag == 'lines':
                                for line in classContest:
                                    className = testClass.attrib['name']
                                    lineNumber = line.attrib['number']
                                    if line.attrib['hits'] == '1':
                                        try:
                                            cover[className].add(lineNumber)
                                        except KeyError:
                                            cover[className] = {lineNumber}
                                    else:
                                        try:
                                            uncover[className].add(lineNumber)
                                        except KeyError:
                                            uncover[className] = {lineNumber}

    #insert rows
    print("----------- Coverage -----------")
    print(cover)
    print(uncover)
    print(sum_rows)
    print(coverarge_rows)

def parseAnnotate(directory):
    if os.path.isdir(directory):
        for filename in os.listdir(directory):
            if filename.endswith(",cover"):
                parseAnnotateFile(directory + "\\" + filename) #TODO fix \\
    if os.path.isfile(directory):
        parseAnnotateFile(directory)

def parseAnnotateFile(file_path):
    function_details_rows = []
    runId = 0
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
            function_details_rows.append([runId, file_name, function_name, is_tested])
    print(function_details_rows)

if __name__ == "__main__":

    # os.system("pytest --cov-report xml --cov=C:\\Users\\GL\Documents\\Year_3\\Open_Workshop\\Coderage C:\\Users\\GL\\Documents\\Year_3\\Open_Workshop\\Coderage\\Tests_Examples\\tests.py --junitxml=filetest.xml")

    parsePytest("C:\\Users\\GL\\Documents\\Year_3\\Open_Workshop\\Coderage\\Tests_Examples\\filetest.xml")
    parseCoverage("C:\\Users\\GL\\Documents\\Year_3\\Open_Workshop\\Coderage\\Tests_Examples\\coverage.xml")
    parseAnnotate("C:\\Users\\GL\\Documents\\Year_3\\Open_Workshop\\Coderage\\covers\\code1.py,cover")
