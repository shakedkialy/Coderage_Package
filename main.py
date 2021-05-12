import sys
from Parser import *
from DatabaseHandler import *

if __name__ == "__main__":
    code_path = sys.argv[1]
    test_path = sys.argv[2]
    output_path = sys.argv[3]

    db = DatabaseHandler(output_path)
    os.system(
        "python -m pytest --cov-report xml:%(Covxml)s --cov=%(code_path)s %(test_path)s --junitxml=%(Testsxml)s" % {"code_path": code_path,
                                                                                               "test_path": test_path, "Covxml": output_path + "/coverage.xml", "Testsxml": output_path + "/tests.xml"})
    parser = Parser(db, output_path)
