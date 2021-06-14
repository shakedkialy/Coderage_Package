# OpenSourceWorkshop - Coderage
<img src="https://github.com/shakedkialy/Coderage/blob/main/html_files/logo.png?raw=true" width="250">

Coderage is a package that allows running tests and code coverage in comparison over time.
The purpose of this project is to enable easy and efficient analyzing and conclusion drawing regarding software testing.


## Requirements for Installing:  
- `git clone https://github.com/shakedkialy/Coderage.git`
- packages : 
  - `pip install pytest` 
  - `pip install pytest-cov`
  -  `pip install pytest-html`

## Test Your Installment:
* If you clone our files in git, code and code2 folders contain 2 code modules for example. Tests_Examples contains pytest test for those modules. \
This command runs coverage on the whole directory (ignores the package files and runs coverage on code and code2) and runs the test in the Tests_Examples folder:
```python main.py module=. tests=Tests_Examples```

After this command line script is complete, you should see the following message:

      Coverage annotated source written to dir Results\annotate
      Coverage HTML written to dir Results\html
      Coverage XML written to file Results\coverage.xml

## Usage Instructions
  
1. Add ```__ init__.py``` file to the code package you want to test. 
2. Name your test files ```*test.py``` 

* In order to run Coderage you can use the following command:
`python main.py module=module1,module2 tests=test1,test2 out_dir=results`

## Results
* The Coderage results located under ```Results``` folder in your project directory. Results folder created after at least one run.
  * ```Results\html``` contains HTML files where you can find graphs and analysis of your last run. \
  * ```Results\coverage```
  * ```Results\annotate```
 
 * To view the results of this package open main_index.html (located in <full_path_to_Coderage_project>/Results/html/main_index.html) via any web browser and navigate from there to all the reports.
