import sys
from Parser import *

if __name__ == "__main__":
    code_path = sys.argv[1]
    test_path = sys.argv[2]

    print("pytest --cov-report xml --cov=%(code_path)s %(test_path)s --junitxml=filetest.xml" % {"code_path": code_path, "test_path": test_path})
    os.system("pytest --cov-report xml --cov=%(code_path)s %(test_path)s --junitxml=filetest.xml" % {"code_path": code_path, "test_path": test_path})

    # parsePytest("C:\\Users\\GL\\Documents\\Year_3\\Open_Workshop\\Coderage\\Tests_Examples\\filetest.xml")
    # parseCoverage("C:\\Users\\GL\\Documents\\Year_3\\Open_Workshop\\Coderage\\Tests_Examples\\coverage.xml")
    # parseAnnotate("C:\\Users\\GL\\Documents\\Year_3\\Open_Workshop\\Coderage\\covers\\code1.py,cover")
