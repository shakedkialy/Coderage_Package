from HTML_TEMPLATES import *
from JS_TEMPLATES import *
import os
import shutil

class HTML:

    def copy_folder_content(self):
        html_files = os.path.join(os.path.abspath(os.path.join(__file__, "..")), "html_files")

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        for item in os.listdir(html_files):
            s = os.path.join(html_files, item)
            d = os.path.join(self.output_path, item)
            if os.path.isdir(s):
                shutil.copytree(s, d)
            else:
                if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                    shutil.copy2(s, d)

    def __init__(self, output_path, db):
        self.output_path = output_path
        self.db = db
        self.copy_folder_content()
        self.generating_highcharts2_js()
        self.generating_detailed_last_run_html()
        self.generating_coverage_analysis_html()
        self.generating_highCharts_js()
        self.generating_test_analysis_html()
        self.generating_main_html()

    def create_table_rows(self, data):
        rows_html = ""
        for row in data:
            row_html = """<tr class=file>
                        <td class="name left">{}</td>\n""".format(row[0])
            for i in range(1,len(row)):
                    row_html += """<td>{}</td>\n""".format(row[i])
            row_html += """</tr>\n"""
            rows_html += row_html
        return rows_html


    def generating_main_html(self):
        main_table = self.db.get_main_table()
        with open(os.path.join(self.output_path, "main_index.html"), 'w') as f:
            message = MAIN_HTML_MSG.format(main_table=main_table)
            f.write(message)


    def generating_highCharts_js(self):
        test_start, passed, failed, skipped = self.db.get_main_test_history()
        cov_start, cover = self.db.get_main_coverage_history()
        with open(os.path.join(self.output_path, "highchart.js"), 'w') as f:
            message = HIGHCHARTS_MSG.format(test_start, passed, failed, skipped, cov_start, cover)
            f.write(message)

    def generating_highcharts2_js(self):
        runid, tested, not_tested = self.db.get_last_tested_vs_not()
        with open(os.path.join(self.output_path, "highchart2.js"), 'w') as f:
            message = HIGHCHARTS2_MSG.format(runid, tested, not_tested)
            f.write(message)


    def generating_coverage_analysis_html(self):
        data = self.db.get_file_coverage()
        table = self.create_table_rows(data)
        with open(os.path.join(self.output_path, "coverageAnalysis.html"), 'w') as f:
            message = COVERAGE_HTML_ANALYSIS.format(table)
            f.write(message)

    def generating_detailed_last_run_html(self):
        untested_data = self.db.get_last_untested()
        untested_table = self.create_table_rows(untested_data)

        changed_functions_data = self.db.get_last_changed_functions()
        changed_functions_table = self.create_table_rows(changed_functions_data)

        changed_tests_data = self.db.get_last_changed_tests()
        changed_tests_table = self.create_table_rows(changed_tests_data)

        with open(os.path.join(self.output_path, "detailedLastRun.html"), 'w') as f:
            message = DETAILED_LAST_RUN.format(untested_table, changed_functions_table, changed_tests_table)
            f.write(message)

    def generating_test_analysis_html(self):
        vs_data = self.db.get_file_tested_vs_not()
        vs_table = self.create_table_rows(vs_data)

        test_history_data = self.db.get_file_test_history()
        test_history_table = self.create_table_rows(test_history_data)

        did_pass_data = self.db.get_file_tests_did_pass()
        did_pass_table = self.create_table_rows(did_pass_data)

        with open(os.path.join(self.output_path, "testAnalysis.html"), 'w') as f:
            message = TEST_ANALYSIS.format(vs_table,test_history_table, did_pass_table)
            f.write(message)


