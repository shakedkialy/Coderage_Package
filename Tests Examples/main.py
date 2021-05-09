import os
import xml.etree.ElementTree as et

# Syntax examples:

# Using pytest-cov
# os.system("pytest --cov-report xml --cov=C:\\Users\\Doron\\Desktop\\OpenSource\\parsing C:\\Users\\Doron\\Desktop\\OpenSource\\parsing\\tests.py --junitxml=filetest.xml")

# Generate the pytest results xml -
# os.system("coverage run -m pytest C:\\Users\\Doron\\Desktop\\OpenSource\\parsing\\tests.py --junitxml=filetest.xml")

# Generate the xml coverage report - without "include" will get all the classes that run
# os.system("coverage xml --include=C:\\Users\\Doron\\Desktop\\OpenSource\\parsing*")

def parsePytest():
    tree = et.parse("C:\\Users\\Doron\\Desktop\\OpenSource\\parsing\\filetest.xml")
    root = tree.getroot()

    passTests = {}
    failTests = {}
    for element in root:
        for child in element:
            if not len(child):
                passTests[child.attrib["name"]] = child.attrib["classname"]
            else:
                for grandchild in child:
                    failTests[child.attrib["name"]] = grandchild.text

    print("----------- Passed / Failed -----------")
    print(passTests)
    print(failTests)

def parseCoverage():
    tree = et.parse("C:\\Users\\Doron\\Desktop\\OpenSource\\parsing\\coverage.xml")
    root = tree.getroot()

    cover = {}
    uncover = {}
    for element in root:
        if element.tag == 'packages':
            for package in element:
                for classes in package:
                    for testClass in classes:
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
    print("----------- Coverage -----------")
    print(cover)
    print(uncover)

if __name__ == "__main__":

    os.system("pytest --cov-report xml --cov=C:\\Users\\Doron\\Desktop\\OpenSource\\parsing C:\\Users\\Doron\\Desktop\\OpenSource\\parsing\\tests.py --junitxml=filetest.xml")

    parsePytest()
    parseCoverage()

    # os.system("coverage run -m pytest C:\\Users\\Doron\\Desktop\\OpenSource\\parsing\\tests.py --junitxml=filetest.xml")
    # os.system("coverage run --branch C:\\Users\\Doron\\Desktop\\OpenSource\\parsing\\tests.py")

    # os.system("coverage report -m --include=C:\\Users\\Doron\\Desktop\\OpenSource\\parsing*")
    # os.system("coverage xml --include=C:\\Users\\Doron\\Desktop\\OpenSource\\parsing*")
    # os.system("coverage html --include=C:\\Users\\Doron\\Desktop\\OpenSource\\parsing*")

    # subprocess.call(["coverage", "html", "pytest", "C:\\Users\\Doron\\Desktop\\OpenSource\\parsing\\tests.py", "--junitxml=filetest.xml"])


