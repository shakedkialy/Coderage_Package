import sys
from Parser import *
from DatabaseHandler import *

def parse_args(argv):
    code_path, test_path, output_path, extra_args = "", "", "", ""
    for arg in argv:
        if "module" in arg:
            modules = arg.split("=")[1]
            code_path = modules.split(",")
        if "tests" in arg:
            test_path = arg.split("=")[1]
        if "out_dir" in arg:
            output_path = arg.split("=")[1]
        if len(sys.argv) > 4:
            extra_args = sys.argv[4:len(sys.argv)]
        extra_args = " ".join(extra_args)
    if code_path == "":
        raise Exception("Missing modules to cover")
    if test_path == "":
        test_path = "Tests"
    if output_path == "":
        output_path = "Results"
    return code_path, test_path, output_path, extra_args


if __name__ == "__main__":
    code_path, test_path, output_path, extra_args = parse_args(sys.argv)

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
        " %(test_path)s --junitxml=%(Testsxml)s %(extra_args)s" % {
            "cov_modules": cov_modules,
            "test_path": test_path,
            "Covxml": output_path + "/coverage.xml",
            "Testsxml": output_path + "/tests.xml",
            "cov_annotate": output_path + "/annotate",
            "extra_args": extra_args})
    parser = Parser(db, output_path)

    # python main.py module=. tests=Tests_Examples\

