import sqlite3
from sqlite3 import Error


class DatabaseHandler:
    __SQL_CREATE_TESTS_DETAILS = """CREATE TABLE IF NOT EXISTS tests_details(  
                                  run_id integer,
                                  class_name text,
                                  test_name text, 
                                  did_pass integer CHECK(did_pass=1 or did_pass=0),
                                  error text,
                                  run_time text,
                                  PRIMARY KEY(run_id, class_name, test_name)
                                  FOREIGN KEY (run_id) REFERENCES run_summary (run_id)
                                  );"""

    __SQL_CREATE_RUN_SUMMARY = """CREATE TABLE IF NOT EXISTS run_summary(
                                run_id integer PRIMARY KEY,
                                errors integer,
                                passed integer,
                                failed integer,
                                skipped integer,
                                run_time text,
                                timestemp text
                                );"""

    __SQL_CREATE_COVERAGE = """CREATE TABLE IF NOT EXISTS coverage(
                                run_id integer,
                                line_rate real,
                                package_name text,
                                file_name text,
                                class_name text,
                                PRIMARY KEY(run_id, package_name, file_name, class_name)
                                FOREIGN KEY (run_id) REFERENCES run_summary (run_id)
                                );"""

    __SQL_CREATE_COVERAGE_SUMMARY = """CREATE TABLE IF NOT EXISTS coverage_summary(
                                      run_id integer PRIMARY KEY,
                                      line_rate real,
                                      lines_valid integer,
                                      timestemp text,
                                      FOREIGN KEY (run_id) REFERENCES run_summary (run_id)
                                    );"""

    __SQL_CREATE_FUNCTIONS_DETAILS = """CREATE TABLE IF NOT EXISTS functions_details(
                                      run_id integer,
                                      file_name text,
                                      function_name text,
                                      is_tested integer CHECK(is_tested=1 or is_tested=0),
                                      PRIMARY KEY(run_id, file_name, file_name, function_name)
                                      FOREIGN KEY (run_id) REFERENCES run_summary (run_id)
                                    );"""

    __SQL_INSERT_TESTS_DETAILS = """INSERT INTO tests_details(run_id,class_name,test_name,did_pass,error,run_time)
                                VALUES(?,?,?,?,?,?)"""

    __SQL_INSERT_RUN_SUMMARY = """INSERT INTO run_summary(run_id,errors,passed,failed,skipped,run_time,timestemp)
                                VALUES(?,?,?,?,?,?,?)"""

    __SQL_INSERT_COVERAGE = """INSERT INTO coverage(run_id,line_rate,package_name,file_name,class_name)
                                VALUES(?,?,?,?,?)"""

    __SQL_INSERT_COVERAGE_SUMMARY = """INSERT INTO coverage_summary(run_id,line_rate,lines_valid,timestemp)
                                VALUES(?,?,?,?)"""

    __SQL_INSERT_FUNCTIONS_DETAILS = """INSERT INTO functions_details(run_id,file_name,function_name,is_tested)
                                VALUES(?,?,?,?)"""

    def __add_table(self, create_table_sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(e)

    def __create_tables(self):
        self.__add_table(DatabaseHandler.__SQL_CREATE_TESTS_DETAILS)
        self.__add_table(DatabaseHandler.__SQL_CREATE_RUN_SUMMARY)
        self.__add_table(DatabaseHandler.__SQL_CREATE_COVERAGE)
        self.__add_table(DatabaseHandler.__SQL_CREATE_COVERAGE_SUMMARY)
        self.__add_table(DatabaseHandler.__SQL_CREATE_FUNCTIONS_DETAILS)

    def __open_connection(self):
        try:
            self.connection = sqlite3.connect(self.projectPath)
            return True

        except Error as e:
            self.connection = None
            print("Can't create Codearge database: " + str(e))
            return False

    def __init__(self, project_path):
        self.projectPath = project_path + "/coderage.db"
        self.connection = None

        if not self.__open_connection():
            exit(1)

        self.__create_tables()
        self.connection.close()

    def __insert_to_table(self, sql_command, data):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        self.__open_connection()
        for line in data:
            cur = self.connection.cursor()
            cur.execute(sql_command, line)
            self.connection.commit()

    def insert_tests_details(self, data):
        self.__insert_to_table(DatabaseHandler.__SQL_INSERT_TESTS_DETAILS, data)

    def insert_run_summary(self, data):
        self.__insert_to_table(DatabaseHandler.__SQL_INSERT_RUN_SUMMARY, data)

    def insert_coverage(self, data):
        self.__insert_to_table(DatabaseHandler.__SQL_INSERT_COVERAGE, data)

    def insert_coverage_summary(self, data):
        self.__insert_to_table(DatabaseHandler.__SQL_INSERT_COVERAGE_SUMMARY, data)

    def insert_functions_details(self, data):
        self.__insert_to_table(DatabaseHandler.__SQL_INSERT_FUNCTIONS_DETAILS, data)

    def select_all(self):
        self.__open_connection()
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM functions_details")

        rows = cur.fetchall()

        # for row in rows:
        #     print(row)

    def get_last_run_id(self):
        self.__open_connection()
        cur = self.connection.cursor()
        cur.execute("SELECT max(run_id) FROM run_summary")
        rows = cur.fetchall()
        return rows[0][0]



# (r"C:\Users\Doron\Desktop\OpenSource\parsing\coderage.db")