# OpenSourceWorkshop - Coderage
<img src="https://github.com/shakedkialy/Coderage/blob/main/html_files/logo.png?raw=true" width="250"> 
Coderage is a package that allows running tests and code coverage in comparison over time.
The purpose of this project is to enable easy and efficient analyzing and conclusion drawing regarding software testing.

# Project license:
#### MIT

# Packages to install (inside terminal):
    pip install pytest
    pip install pytest-cov
    pip install pytest-html
# How to run:
## General files:
    1. add __ init__.py file to the code package you want to test. 
    2. name your test files *test.py 
    3. go to command line and run the following:
       python main.py module=module1,module2 tests=test1,test2 out_dir=results
## Out tests:
    Go to Coderage directory inside command line and run the following:
    python main.py module=. tests=Tests_Examples
    
     
