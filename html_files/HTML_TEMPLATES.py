MAIN_HTML_MSG = """<!DOCTYPE html>
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
                        <th class="right shortkey_c">Coverage %</th>
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
        <script src="https://code.highcharts.com/modules/data.js"></script>
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
        """

COVERAGE_HTML_ANALYSIS = """"<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Coverage Analysis By File</title>
    <style>
    * {
      box-sizing: border-box;
    }

    .parent {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    img { width: 20%; height: 20%; margin-left: 40%;}
    #myInput {
      background-position: 10px 10px;
      background-repeat: no-repeat;
      width: 100%;
      font-size: 16px;
      padding: 12px 20px 12px 40px;
      border: 1px solid #ddd;
      margin-bottom: 12px;
    }

    #myTable {
      border-collapse: collapse;
      width: 100%;
      border: 1px solid #ddd;
      font-size: 18px;
    }

    #myTable th, #myTable td {
      text-align: left;
      padding: 12px;
    }

    #myTable tr {
      border-bottom: 1px solid #ddd;
    }

    #myTable tr.header, #myTable tr:hover {
      background-color: #f1f1f1;
    }
    </style>
</head>
<body>
<div id="header">
    <div class="content">
        <img src="unnamed.png"></img>
    </div>
</div>

    <br></br>
    <h1>Coverage Analysis By File</h1>
    <br></br>
    <div class="parent">

    <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for file name.." title="Type in a file name">

    <table id="myTable">
      <tr class="header">
        <th style="width:60%;">Name</th>
        <th style="width:40%;">Country</th>
      </tr>
      <tr>
        <td>Alfreds Futterkiste</td>
        <td>Germany</td>
      </tr>
      <tr>
        <td>Berglunds snabbkop</td>
        <td>Sweden</td>
      </tr>
      <tr>
        <td>Island Trading</td>
        <td>UK</td>
      </tr>
      <tr>
        <td>Koniglich Essen</td>
        <td>Germany</td>
      </tr>
      <tr>
        <td>Laughing Bacchus Winecellars</td>
        <td>Canada</td>
      </tr>
      <tr>
        <td>Magazzini Alimentari Riuniti</td>
        <td>Italy</td>
      </tr>
      <tr>
        <td>North/South</td>
        <td>UK</td>
      </tr>
      <tr>
        <td>Paris specialites</td>
        <td>France</td>
      </tr>
    </table>

    <script>
    function myFunction() {
      var input, filter, table, tr, td, i, txtValue;
      input = document.getElementById("myInput");
      filter = input.value.toUpperCase();
      table = document.getElementById("myTable");
      tr = table.getElementsByTagName("tr");
      for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
          txtValue = td.textContent || td.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
          } else {
            tr[i].style.display = "none";
          }
        }
      }
    }
    </script>
</div>
</body>
</html>"""

DETAILED_LAST_RUN = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
     <link rel="stylesheet" href="detailedLastRun.css" type="text/css">
    <title>Detailed Last Run</title>
</head>
<div id="header">
    <div class="content">
        <img src="unnamed.png"></img>
    </div>
</div>
<body>
    <br></br>
    <h1>Detailed Last Run</h1>
    <br></br>
    <div class="parent">
        <p class="graph">graph</p>
        <p class="new">New functions added to coverage:</p>
        <p class="not">Functions still not covered:</p>
        <p class="test">Functions not tested</p>
    </div>
</body>
</html>"""

TEST_ANALYSIS = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Coverage Analysis By File</title>
    <style>
    * {
      box-sizing: border-box;
    }

    .parent {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    img { width: 20%; height: 20%; margin-left: 40%;}
    #myInput {
      background-position: 10px 10px;
      background-repeat: no-repeat;
      width: 100%;
      font-size: 16px;
      padding: 12px 20px 12px 40px;
      border: 1px solid #ddd;
      margin-bottom: 12px;
    }

    #myTable {
      border-collapse: collapse;
      width: 100%;
      border: 1px solid #ddd;
      font-size: 18px;
    }

    #myTable th, #myTable td {
      text-align: left;
      padding: 12px;
    }

    #myTable tr {
      border-bottom: 1px solid #ddd;
    }

    #myTable tr.header, #myTable tr:hover {
      background-color: #f1f1f1;
    }
    </style>
</head>
<body>
<div id="header">
    <div class="content">
        <img src="unnamed.png"></img>
    </div>
</div>

    <br></br>
    <h1>Coverage Analysis By File</h1>
    <br></br>
    <div class="parent">

    <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for file name.." title="Type in a file name">

    <table id="myTable">
      <tr class="header">
        <th style="width:60%;">Name</th>
        <th style="width:40%;">Country</th>
      </tr>
      <tr>
        <td>Alfreds Futterkiste</td>
        <td>Germany</td>
      </tr>
      <tr>
        <td>Berglunds snabbkop</td>
        <td>Sweden</td>
      </tr>
      <tr>
        <td>Island Trading</td>
        <td>UK</td>
      </tr>
      <tr>
        <td>Koniglich Essen</td>
        <td>Germany</td>
      </tr>
      <tr>
        <td>Laughing Bacchus Winecellars</td>
        <td>Canada</td>
      </tr>
      <tr>
        <td>Magazzini Alimentari Riuniti</td>
        <td>Italy</td>
      </tr>
      <tr>
        <td>North/South</td>
        <td>UK</td>
      </tr>
      <tr>
        <td>Paris specialites</td>
        <td>France</td>
      </tr>
    </table>

    <script>
    function myFunction() {
      var input, filter, table, tr, td, i, txtValue;
      input = document.getElementById("myInput");
      filter = input.value.toUpperCase();
      table = document.getElementById("myTable");
      tr = table.getElementsByTagName("tr");
      for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
          txtValue = td.textContent || td.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
          } else {
            tr[i].style.display = "none";
          }
        }
      }
    }
    </script>
</div>
</body>
</html>"""