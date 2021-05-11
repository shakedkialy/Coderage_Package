import sqlite3
from sqlite3 import Error


class Database:
    SQL_CREATE_TESTS_DETAILS = """CREATE TABLE IF NOT EXISTS tests_details(  
                                  run_id integer,
                                  class_name text,
                                  test_name text, 
                                  did_pass integer CHECK(did_pass=1 or did_pass=0),
                                  error text,
                                  run_time text,
                                  PRIMARY KEY(run_id, class_name, test_name)
                                  FOREIGN KEY (run_id) REFERENCES run_summary (run_id)
                                  );"""

    SQL_CREATE_RUN_SUMMARY = """CREATE TABLE IF NOT EXISTS run_summary(
                                run_id integer PRIMARY KEY,
                                errors integer,
                                passed integer,
                                failed integer,
                                skipped integer,
                                run_time text,
                                timestemp text
                                );"""

    SQL_CREATE_COVERAGE = """CREATE TABLE IF NOT EXISTS coverage(
                                run_id integer PRIMARY KEY,
                                line_rate real,
                                package_name text,
                                file_name text,
                                class_name text,
                                PRIMARY KEY(run_id, package_name, file_name, class_name)
                                FOREIGN KEY (run_id) REFERENCES run_summary (run_id)
                                );"""

    SQL_CREATE_COVERAGE_SUMMARY = """CREATE TABLE IF NOT EXISTS coverage_summary(
                                      run_id integer PRIMARY KEY,
                                      line_rate real,
                                      lines_valid integer,
                                      timestemp text,
                                      FOREIGN KEY (run_id) REFERENCES run_summary (run_id)
                                    );"""

    SQL_CREATE_FUNCTIONS_DETAILS = """CREATE TABLE IF NOT EXISTS functions_details(
                                      run_id integer PRIMARY KEY,
                                      file_name text,
                                      function_name text,
                                      is_tested integer CHECK(is_tested=1 or is_tested=0),
                                      PRIMARY KEY(run_id, file_name, file_name, function_name)
                                      FOREIGN KEY (run_id) REFERENCES run_summary (run_id)
                                    );"""

    def __add_table(self, create_table_sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(e)

    def __create_tables(self):
        self.__add_table(Database.SQL_CREATE_TESTS_DETAILS)
        self.__add_table(Database.SQL_CREATE_RUN_SUMMARY)
        self.__add_table(Database.SQL_CREATE_COVERAGE)
        self.__add_table(Database.SQL_CREATE_COVERAGE_SUMMARY)
        self.__add_table(Database.SQL_CREATE_FUNCTIONS_DETAILS)

    def __open_connection(self):
        try:
            self.connection = sqlite3.connect(self.projectPath)

        except Error as e:
            self.connection = None
            print("Can't create Codearge database: " + str(e))

    def __init__(self, project_path):
        self.projectPath = project_path + "\coderage.db"
        self.connection = None

        self.__open_connection()
        if self.connection is None:
            exit(1)

        self.__create_tables()

    def getLastRunID():
        pass


# (r"C:\Users\Doron\Desktop\OpenSource\parsing\coderage.db")