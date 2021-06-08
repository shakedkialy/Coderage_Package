# OpenSourceWorkshop - Coderage
<img src="https://github.com/shakedkialy/Coderage/blob/main/html_files/logo.png?raw=true" width="250"> 
Coderage is a package that allows running tests and code coverage in comparison over time.
The purpose of this project is to enable easy and efficient analyzing and conclusion drawing regarding software testing.


requirements for running: \
    packages: pytest, pytest-cov, pytest-html \
    1. add __ init__.py file to the code package you want to test. \
    2. name your test files *test.py \
    3. command line for example: \
      python main.py module=module1,module2 tests=test1,test2 out_dir=results \
      if you clone our files in git, this command line should work when running from the main folder: \
      __python main.py module=. tests=Tests_Examples__ \
