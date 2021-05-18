import sys
from Parser import *
from DatabaseHandler import *

NUM_ARGS = 5


def parse_args(argv):
    code_path, test_path, output_path, extra_args, delete_out = "", "", "", "", ""
    for arg in argv:
        if "module" in arg:
            modules = arg.split("=")[1]
            code_path = modules.split(",")
        if "tests" in arg:
            test_path = arg.split("=")[1]
        if "out_dir" in arg:
            output_path = arg.split("=")[1]
        if "delete_out" in arg:
            delete_out = arg.split("=")[1]
        if len(sys.argv) > NUM_ARGS:
            extra_args = sys.argv[NUM_ARGS:len(sys.argv)]
        extra_args = " ".join(extra_args)
    if code_path == "":
        raise Exception("Missing modules to cover")
    if test_path == "":
        test_path = "Tests"
    if output_path == "":
        output_path = "Results"
    if delete_out == "False":
        delete_out = False
    if delete_out == "":
        delete_out = True
    return code_path, test_path, output_path, delete_out, extra_args


if __name__ == "__main__":
    code_path, test_path, output_path, delete_out, extra_args = parse_args(sys.argv)

    # TODO: check slashes in windows and linux.
    if not os.path.exists(output_path):
        if not delete_out:
            os.system("mkdir %(output_path)s" % {"output_path": output_path})
        else:
            os.system("mkdir %(output_path)s %(output_path)s\\annotate" % {"output_path": output_path})
    db = DatabaseHandler(output_path)
    cov_modules = ""
    for module in code_path:
        cov_modules += ("--cov=%(code_path)s " % {"code_path": module})

    if not delete_out and os.path.exists(output_path):
        output_path += str(db.get_last_run_id() + 1)

    os.system(
        "python -m pytest --cov-report annotate:%(cov_annotate)s --cov-report html:%(cov_html)s --cov-report xml:%(Covxml)s %(cov_modules)s"
        " %(test_path)s --junitxml=%(Testsxml)s %(extra_args)s" % {
            "cov_modules": cov_modules,
            "test_path": test_path,
            "Covxml": output_path + "/coverage.xml",
            "Testsxml": output_path + "/tests.xml",
            "cov_annotate": output_path + "/annotate",
            "cov_html": output_path + "/html",
            "extra_args": extra_args})

    parser = Parser(db, output_path)
    if delete_out:
        os.system("rm -r %(Covxml)s %(Testsxml)s %(cov_annotate)s %(cov_html)s .hypothesis .pytest_cache" % {
            "Covxml": output_path + "\\coverage.xml",
            "Testsxml": output_path + "\\tests.xml",
            "cov_annotate": output_path + "\\annotate",
            "cov_html": output_path + "\\html"})

    # python main.py module=. tests=Tests_Examples
