from DatabaseHandler import *

class HTML:

    def __init__(self, output_path, db):
        self.output_path = output_path
        self.db = db


    def generating_html(self):
        main_table = self.db.get_main_table()[0]
        code2 = [5,6]
        f = open('html_files\index.html','w')

        message = """<!DOCTYPE html>
        <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>Coderage</title>
            <link rel="icon" sizes="15x15" href="unnamed.png">
            <link rel="stylesheet" href="style.css" type="text/css">
            <link rel="stylesheet" href="highchart.css" type="text/css">
            <script type="text/javascript" src="jquery.min.js"></script>
            <script type="text/javascript">
                jQuery(document).ready(coverage.index_ready);
            </script>
        
        
        
        </head>
        <body class="indexfile">
        <div id="header">
            <div class="content">
                <img src="unnamed.png"></img>
        
                <form id="filter_container">
                    <input id="filter" type="text" value="" placeholder="filter..." />
                </form>
            </div>
        </div>
        
        <div id="index">
            <table class="index">
                <thead>
                    <tr class="tablehead" title="Click to sort">
                        <th class="name left headerSortDown shortkey_n">Run Number</th>
                        <th class="shortkey_s">TestsPath</th>
                        <th class="shortkey_m">Passed</th>
                        <th class="shortkey_x">Failed</th>
                        <th class="right shortkey_c">Errors</th>
                        <th class="right shortkey_c">Skipped</th>
                        <th class="right shortkey_c">Run Time (Sec)</th>
                        <th class="right shortkey_c">Coverage Path</th>
                        <th class="right shortkey_c">Coverage</th>
                        <th class="right shortkey_c">Statments</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="file">
                        <td class="name left">{main_table[0]}</td>
                        <td>{main_table[1]}</td>
                        <td> {main_table[2]}</td>
                        <td>{main_table[3]}</td>
                        <td>{main_table[4]}</td>
                        <td>{main_table[5]}</td>
                        <td>{main_table[6]}</td>
                        <td>{main_table[7]}</td>
                        <td>{main_table[8]}</td>
                        <td>{main_table[9]}</td>
                    </tr>
                </tbody>
            </table>
            <p id="no_rows">
                No items found using the specified filter.
            </p>
        </div>
        <br></br>
        <br></br>
        <div id="footer">
            <div class="content">
                <span>
                    <a class="nav" href="detailedLastRun.html">Detailed Last Ran Analysis</a> 
                </span>
                <span>
                    <a class="nav" href="/">Detailed Tests Results</a> 
                </span>
                <span>
                    <a class="nav" href="/">Detailed Coverage</a> 
                </span>
                <span>
                    <a class="nav" href="coverageAnalysis.html">Coverage Analysis By File</a> 
                </span>
                        <span>
                    <a class="nav" href="testAnalysis.html">Test Analysis By File</a> 
                </span>
            </div>
        </div>
        <br></br>
        
        <script src="https://code.highcharts.com/highcharts.js"></script>
        <script src="https://code.highcharts.com/modules/series-label.js"></script>
        <script src="https://code.highcharts.com/modules/exporting.js"></script>
        <script src="https://code.highcharts.com/modules/export-data.js"></script>
        <script src="https://code.highcharts.com/modules/accessibility.js"></script>
        <script src="https://code.highcharts.com/highcharts-more.js"></script>
        <br></br>
        <br></br>
        <div class="charts">
        <figure class="highcharts-figure">
          <div id="container"></div>
          <p class="highcharts-description">
            Basic line chart showing trends in a dataset. This chart includes the
            <code>series-label</code> module, which adds a label to each line for
            enhanced readability.
          </p>
        </figure>
        
        <figure class="highcharts-figure">
          <div id="container2"></div>
          <p class="highcharts-description">
            Basic line chart showing trends in a dataset. This chart includes the
            <code>series-label</code> module, which adds a label to each line for
            enhanced readability.
          </p>
        </figure>
        
        </div>
        <script type="text/javascript" src="highchart.js"></script>
        </body>
        </html>
        """.format(main_table=main_table, code2=code2)

        f.write(message)
        f.close()
