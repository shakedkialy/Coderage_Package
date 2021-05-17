import sys
from Parser import *
from DatabaseHandler import *


if __name__ == "__main__":
    #TODO: more elegant way to parse modules. add names for parameters
    num_modules = int(sys.argv[1])
    code_path = []
    for i in range(num_modules):
        code_path.append(sys.argv[2 + i])
    test_path = sys.argv[2 + num_modules]
    output_path = sys.argv[3 + num_modules]

    # TODO: check slashes in windows and linux.
    if not os.path.exists(output_path):
        os.system("mkdir %(output_path)s %(output_path)s\\annotate" % {"output_path": output_path})
    db = DatabaseHandler(output_path)
    cov_modules = ""
    for module in code_path:
        cov_modules += ("--cov=%(code_path)s " % {"code_path": module})

    # TODO: how to not run coverage on __init__?
    os.system(
        "python -m pytest --cov-report annotate:%(cov_annotate)s --cov-report xml:%(Covxml)s %(cov_modules)s"
        " %(test_path)s --junitxml=%(Testsxml)s" % {
            "cov_modules": cov_modules,
            "test_path": test_path,
            "Covxml": output_path + "/coverage.xml",
            "Testsxml": output_path + "/tests.xml",
            "cov_annotate": output_path + "/annotate"})
    parser = Parser(db, output_path)

    # python main.py code1 Tests_Examples\b_test.py Results
    # python main.py 1 . Tests_Examples\ Results

