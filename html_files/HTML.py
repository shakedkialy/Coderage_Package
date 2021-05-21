from DatabaseHandler import *
from html_files.HTML_TEMPLATES import *
from html_files.JS_TEMPLATES import *
class HTML:

    def __init__(self, output_path, db):
        self.output_path = output_path
        self.db = db

    def generating_main_html(self):
        main_table = self.db.get_main_table()[0]
        code2 = [5, 6]
        with open('html_files\index.html', 'w') as f:

            message = MAIN_HTML_MSG.format(main_table=main_table, code2=code2)
            f.write(message)


    def generating_highCharts_js(self):
        test_start, passed, failed, skipped = self.db.get_main_test_history()
        cov_start, cover = self.db.get_main_coverage_history()
        with open('html_files\highchart.js', 'w') as f:

            message = HIGHCHARTS_MSG.format(test_start, passed, failed, skipped, cov_start, cover)
            f.write(message)


    def generating_coverage_analysis_html(self):
        data = []
        with open('html_files\coverageAnalysis.html', 'w') as f:

            message = COVERAGE_HTML_ANALYSIS.format(data=data)
            f.write(message)

    def generating_detailed_last_run_html(self):
        data = []
        with open('html_files\detailedLastRun.html', 'w') as f:

            message = DETAILED_LAST_RUN.format(data=data)
            f.write(message)

    def generating_test_analysis_html(self):
        data = []
        with open('html_files\/testAnalysis.html', 'w') as f:

            message = DETAILED_LAST_RUN.format(data=data)
            f.write(message)
