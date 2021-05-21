import sqlite3
from sqlite3 import Error
import SQLQueries

class DatabaseHandler:
    RESULTS_LIMIT = 10

    def __execute_query(self, query):
        self.__open_connection()
        cur = self.connection.cursor()
        cur.execute(query)

        return cur.fetchall()

    def __add_table(self, create_table_sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(e)

    def __create_tables(self):
        self.__add_table(SQLQueries.CREATE_TESTS_DETAILS)
        self.__add_table(SQLQueries.CREATE_RUN_SUMMARY)
        self.__add_table(SQLQueries.CREATE_COVERAGE)
        self.__add_table(SQLQueries.CREATE_COVERAGE_SUMMARY)
        self.__add_table(SQLQueries.CREATE_FUNCTIONS_DETAILS)

    def __open_connection(self):
        try:
            self.connection = sqlite3.connect(self.projectPath)
            return True

        except Error as e:
            self.connection = None
            print("Can't create Codearge database: " + str(e))
            return False

    def get_last_run_id(self):
        rows = self.__execute_query("SELECT max(run_id) FROM run_summary")
        if rows[0][0] is None:
            return 0
        return rows[0][0]

    def __init__(self, project_path):
        self.projectPath = project_path + "/coderage.db"
        self.connection = None

        if not self.__open_connection():
            exit(1)

        self.__create_tables()
        self.connection.close()

    """
    ----- Inserting data to the tables ----
    """

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
        self.__insert_to_table(SQLQueries.INSERT_TESTS_DETAILS, data)

    def insert_run_summary(self, data):
        self.__insert_to_table(SQLQueries.INSERT_RUN_SUMMARY, data)

    def insert_coverage(self, data):
        self.__insert_to_table(SQLQueries.INSERT_COVERAGE, data)

    def insert_coverage_summary(self, data):
        self.__insert_to_table(SQLQueries.INSERT_COVERAGE_SUMMARY, data)

    def insert_functions_details(self, data):
        self.__insert_to_table(SQLQueries.INSERT_FUNCTIONS_DETAILS, data)

    """
    ----- Html - Main page ----
    """

    def get_main_table(self):
        return self.__execute_query(SQLQueries.MAIN_TABLE)

    def get_main_test_history(self):
        return self.__execute_query(SQLQueries.MAIN_TESTS_HISTORY.format(DatabaseHandler.RESULTS_LIMIT))

    def get_main_coverage_history(self):
        return self.__execute_query(SQLQueries.MAIN_COVERAGE_HISTORY.format(DatabaseHandler.RESULTS_LIMIT))

    """
    ----- Html - Last run analysis page ----
    """

    def get_last_tested_vs_not(self):
        return self.__execute_query(SQLQueries.LAST_TESTED_VS_NOT_GRAPH.format(DatabaseHandler.RESULTS_LIMIT))

    def get_last_untested(self):
        return self.__execute_query(SQLQueries.LAST_UNTESTED_LIST)

    def get_last_changed_functions(self):
        return self.__execute_query(SQLQueries.LAST_CHANGED_FUNCTIONS_LIST)

    def get_last_changed_tests(self):
        return self.__execute_query(SQLQueries.LAST_CHANGED_TESTS_LIST)

    """
    ----- Html - Coverage Analysis By File page ----
    """

    def get_file_coverage(self, file_name):
        return self.__execute_query(SQLQueries.COVERAGE_FILE_GRAPH.format(file_name, DatabaseHandler.RESULTS_LIMIT))

    """
    ----- Html - Test Analysis By File ----
    """

    def get_file_tested_vs_not(self, file_name):
        return self.__execute_query(SQLQueries.TESTS_FILE_TESTED_VS_NOT_GRAPH.format(file_name, DatabaseHandler.RESULTS_LIMIT))

    def get_file_test_history(self, file_name):
        return self.__execute_query(SQLQueries.TESTS_FILE_HISTORY_GRAPH.format(file_name, DatabaseHandler.RESULTS_LIMIT))

    def get_file_tests_did_pass(self, file_name):
        return self.__execute_query(SQLQueries.TESTS_FILE_DID_PASS.format(file_name))