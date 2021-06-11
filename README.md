# OpenSourceWorkshop - Coderage
<img src="https://github.com/shakedkialy/Coderage/blob/main/html_files/logo.png?raw=true" width="250"> 
Coderage is a package that allows running tests and code coverage in comparison over time.
The purpose of this project is to enable easy and efficient analyzing and conclusion drawing regarding software testing.



## Requirements for running

1. **Install packages:** pytest, pytest-cov, pytest-html. \
   You can install using pip install or using your IDE.
2. Add ```__ init__.py``` file to the code package you want to test. 
3. Name your test files ```*test.py``` 


## Usage
* In order to run Coderage you can use the following command:
`python main.py module=module1,module2 tests=test1,test2 out_dir=results`

    
* If you clone our files in git, code and code2 folders contain 2 code modules for example. Tests_Examples contains pytest test for those modules. \
This command runs coverage on the whole directory (ignores the package files and runs coverage on code and code2) and runs the test in the Tests_Examples folder:
```python main.py module=. tests=Tests_Examples```
    
* The Coderage results located under ```Results``` folder in your project directory. Results folder created after at least one run.
  * ```Results\html``` contains HTML files where you can find graphs and analysis of your last run. \
       **Important Files:** testAnalysis.html, detailedLastRun.html, main_index.html
  * ```Results\coverage```
  * ```Results\annotate```