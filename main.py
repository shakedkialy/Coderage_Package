import sys
from Parser import *
from DatabaseHandler import *

if __name__ == "__main__":
    code_path = sys.argv[1]
    test_path = sys.argv[2]
    output_path = sys.argv[3]

    db = DatabaseHandler(output_path)
    if isinstance(code_path, str):
        cov_modules = ("--cov=%(code_path)s" % {"code_path": code_path})
    else:
        cov_modules = "sss"

    os.system(
        "python -m pytest --cov-report annotate:%(cov_annotate)s --cov-report xml:%(Covxml)s %(cov_modules)s %(test_path)s --junitxml=%(Testsxml)s" % {
            "cov_modules": cov_modules,
            "test_path": test_path, "Covxml": output_path + "/coverage.xml", "Testsxml": output_path + "/tests.xml",
            "cov_annotate": output_path + "/annotate"})
    parser = Parser(db, output_path)

    # python main.py code1 Tests_Examples\tests.py Results

