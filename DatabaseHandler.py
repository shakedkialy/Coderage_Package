import sqlite3
from sqlite3 import Error
import SQLQueries

class DatabaseHandler:
    """
    This class implement a DatabaseHandler - the interface to the DB which holds all the information need to create
    the html files.
    """
    RESULTS_LIMIT = 20

    def __execute_query(self, query):
        """
        :param query: query to execute
        :return: all the rows returned by the query
        """
        self.__open_connection()
        cur = self.connection.cursor()
        cur.execute(query)

        return cur.fetchall()

    def __add_table(self, create_table_sql):
        """
        adds a table to the DB
        :param create_table_sql: the SQL statement that creates the table.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(e)

    def __create_tables(self):
        """
        creates all the tables necessary for the project.
        """
        self.__add_table(SQLQueries.CREATE_TESTS_DETAILS)
        self.__add_table(SQLQueries.CREATE_RUN_SUMMARY)
        self.__add_table(SQLQueries.CREATE_COVERAGE)
        self.__add_table(SQLQueries.CREATE_COVERAGE_SUMMARY)
        self.__add_table(SQLQueries.CREATE_FUNCTIONS_DETAILS)

    def __open_connection(self):
        """
        tries to open a connection with the DB
        :return: True if the connection was creates successfully, False otherwise.
        """
        try:
            self.connection = sqlite3.connect(self.projectPath)
            return True

        except Error as e:
            self.connection = None
            print("Can't create Codearge database: " + str(e))
            return False

    def get_last_run_id(self):
        """
        :return: the last runId from the DB
        """
        rows = self.__execute_query("SELECT max(run_id) FROM run_summary")
        if rows[0][0] is None:
            return 0
        return rows[0][0]

    def __init__(self, project_path, code_path, test_path):
        """
        inits a DB object.
        :param project_path: the directory the project runs in
        :param code_path: the directory of the code
        :param test_path: the directory of the tests
        """
        self.projectPath = project_path + "/coderage.db"
        self.connection = None
        self.code_path = code_path
        self.test_path = test_path

        if not self.__open_connection():
            exit(1)

        self.__create_tables()
        self.connection.close()

    """
    ----- Inserting data to the tables ----
    """

    def __insert_to_table(self, sql_command, data):
        """
        inserts data to table
        :param sql_command: the command that inserts that data
        :param data: the data to insert
        """
        self.__open_connection()
        for line in data:
            cur = self.connection.cursor()
            cur.execute(sql_command, line)
            self.connection.commit()

    def insert_tests_details(self, data):
        """
        inserts data to tests_details table
        :param data:  the data to insert
        """
        self.__insert_to_table(SQLQueries.INSERT_TESTS_DETAILS, data)

    def insert_run_summary(self, data):
        """
        inserts data to run_summary table
        :param data:  the data to insert
        """
        self.__insert_to_table(SQLQueries.INSERT_RUN_SUMMARY, data)

    def insert_coverage(self, data):
        """
        inserts data to coverage table
        :param data:  the data to insert
        """
        self.__insert_to_table(SQLQueries.INSERT_COVERAGE, data)

    def insert_coverage_summary(self, data):
        """
        inserts data to coverage_summary table
        :param data:  the data to insert
        """
        self.__insert_to_table(SQLQueries.INSERT_COVERAGE_SUMMARY, data)

    def insert_functions_details(self, data):
        """
        inserts data to functions_details table
        :param data:  the data to insert
        """
        self.__insert_to_table(SQLQueries.INSERT_FUNCTIONS_DETAILS, data)

    """
    ----- Html - Main page ----
    """

    def get_main_table(self):
        query = self.__execute_query(SQLQueries.MAIN_TABLE)[0]
        main_table = [query[0]] + [self.test_path] + list(query[1:6]) + [self.code_path] + list(query[6:])
        return main_table

    def get_main_test_history(self):
        query = self.__execute_query(SQLQueries.MAIN_TESTS_HISTORY.format(DatabaseHandler.RESULTS_LIMIT))
        first_run_id = query[len(query)-1][0]
        passed = []
        failed = []
        skipped = []
        for row in query:
            passed.append(row[1])
            failed.append(row[2])
            skipped.append(row[3])

        passed.reverse()
        failed.reverse()
        skipped.reverse()

        return first_run_id, passed, failed, skipped

    def get_main_coverage_history(self):
        query = self.__execute_query(SQLQueries.MAIN_COVERAGE_HISTORY.format(DatabaseHandler.RESULTS_LIMIT))
        first_run_id = query[len(query)-1][0]
        results = []
        for row in query:
            results.append(row[1])

        results.reverse()

        return first_run_id, results

    """
    ----- Html - Last run analysis page ----
    """

    def get_last_tested_vs_not(self):
        query = self.__execute_query(SQLQueries.LAST_TESTED_VS_NOT_GRAPH.format(DatabaseHandler.RESULTS_LIMIT))
        runid = []
        tested = []
        not_tested = []
        for row in query:
            runid.append(row[0])
            tested.append(row[1])
            not_tested.append(row[2])

        runid.reverse()
        tested.reverse()
        not_tested.reverse()

        return runid, tested, not_tested

    def get_last_untested(self):
        return self.__execute_query(SQLQueries.LAST_UNTESTED_LIST)

    def get_last_changed_functions(self):
        return self.__execute_query(SQLQueries.LAST_CHANGED_FUNCTIONS_LIST)

    def get_last_changed_tests(self):
        return self.__execute_query(SQLQueries.LAST_CHANGED_TESTS_LIST)

    """
    ----- Html - Coverage Analysis By File page ----
    """

    def get_file_coverage(self):
        return self.__execute_query(SQLQueries.COVERAGE_FILE.format(DatabaseHandler.RESULTS_LIMIT))

    """
    ----- Html - Test Analysis By File ----
    """

    def get_file_tested_vs_not(self):
        return self.__execute_query(SQLQueries.TESTS_FILE_TESTED_VS_NOT.format(DatabaseHandler.RESULTS_LIMIT))

    def get_file_test_history(self):
        return self.__execute_query(SQLQueries.TESTS_FILE_HISTORY.format(DatabaseHandler.RESULTS_LIMIT))

    def get_file_tests_did_pass(self):
        return self.__execute_query(SQLQueries.TESTS_FILE_DID_PASS)
