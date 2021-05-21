"""
----- Creating the tables ----
"""

CREATE_TESTS_DETAILS = """CREATE TABLE IF NOT EXISTS tests_details(  
                                  run_id integer,
                                  class_name text,
                                  test_name text, 
                                  did_pass integer CHECK(did_pass=1 or did_pass=0),
                                  error text,
                                  run_time text,
                                  PRIMARY KEY(run_id, class_name, test_name)
                                  FOREIGN KEY (run_id) REFERENCES run_summary (run_id)
                                  );"""

CREATE_RUN_SUMMARY = """CREATE TABLE IF NOT EXISTS run_summary(
                                run_id integer PRIMARY KEY,
                                errors integer,
                                passed integer,
                                failed integer,
                                skipped integer,
                                run_time text,
                                timestemp text
                                );"""

CREATE_COVERAGE = """CREATE TABLE IF NOT EXISTS coverage(
                                run_id integer,
                                line_rate real,
                                package_name text,
                                file_name text,
                                class_name text,
                                PRIMARY KEY(run_id, package_name, file_name, class_name)
                                FOREIGN KEY (run_id) REFERENCES run_summary (run_id)
                                );"""

CREATE_COVERAGE_SUMMARY = """CREATE TABLE IF NOT EXISTS coverage_summary(
                                      run_id integer PRIMARY KEY,
                                      line_rate real,
                                      lines_valid integer,
                                      timestemp text,
                                      FOREIGN KEY (run_id) REFERENCES run_summary (run_id)
                                    );"""

CREATE_FUNCTIONS_DETAILS = """CREATE TABLE IF NOT EXISTS functions_details(
                                      run_id integer,
                                      file_name text,
                                      function_name text,
                                      is_tested integer CHECK(is_tested=1 or is_tested=0),
                                      PRIMARY KEY(run_id, file_name, file_name, function_name)
                                      FOREIGN KEY (run_id) REFERENCES run_summary (run_id)
                                    );"""

"""
----- Inserting data to the tables ----
"""

INSERT_TESTS_DETAILS = """INSERT INTO tests_details(run_id,class_name,test_name,did_pass,error,run_time)
                                VALUES(?,?,?,?,?,?)"""

INSERT_RUN_SUMMARY = """INSERT INTO run_summary(run_id,errors,passed,failed,skipped,run_time,timestemp)
                                VALUES(?,?,?,?,?,?,?)"""

INSERT_COVERAGE = """INSERT INTO coverage(run_id,line_rate,package_name,file_name,class_name)
                                VALUES(?,?,?,?,?)"""

INSERT_COVERAGE_SUMMARY = """INSERT INTO coverage_summary(run_id,line_rate,lines_valid,timestemp)
                                VALUES(?,?,?,?)"""

INSERT_FUNCTIONS_DETAILS = """INSERT INTO functions_details(run_id,file_name,function_name,is_tested)
                                VALUES(?,?,?,?)"""

"""
----- Html - Main page ----
"""

MAIN_TABLE = """SELECT rs.run_id, rs.passed, rs.failed, rs.errors, rs.failed, rs.run_time, cv.line_rate*100, cv.lines_valid
                FROM run_summary rs
                left join coverage_summary cv
                on rs.run_id = cv.run_id
                where rs.run_id in (select max(run_id)
                                    from run_summary)"""

MAIN_TESTS_HISTORY = """SELECT rs.run_id, rs.passed, rs.failed, rs.skipped
                            FROM run_summary rs
                            order by run_id desc
                            limit {}"""

MAIN_COVERAGE_HISTORY = """SELECT cs.run_id, cs.line_rate*100 as percent
                                FROM coverage_summary cs 
                                order by run_id desc
                                limit {}"""

"""
----- Html - Last run analysis page ----
"""

LAST_TESTED_VS_NOT_GRAPH = """select *
                                from (SELECT fd.run_id, 
                                        COUNT(case when is_tested = 1 then 1 end) as test,
                                        COUNT(case when is_tested = 0 then 1 end) as notTest
                                FROM functions_details fd
                                group by fd.run_id)
                                order by run_id desc
                                limit {}"""  # function_details

LAST_UNTESTED_LIST = """SELECT fd.file_name, fd.function_name
                        FROM functions_details fd
                        where fd.is_tested = 0
                        and fd.run_id in (select max(run_id)
                                          from functions_details)"""  # function_details

LAST_CHANGED_FUNCTIONS_LIST = """SELECT fd.file_name, fd.function_name, 
                                case fd.is_tested when 1 then "Tested" when 0 then "Not Tested" end as cur_run,
                                case fd2.is_tested when 1 then "Tested" when 0 then "Not Tested" else "Doesn't Exist" end as prev_run
                        FROM functions_details fd
                        left join functions_details fd2
                        on fd2.run_id = fd.run_id - 1
                            and fd2.file_name = fd.file_name
                            and fd2.function_name = fd.function_name
                        where fd.run_id in (select max(run_id)
                                          from functions_details) 
                            and (fd2.is_tested is NULL or fd2.is_tested != fd.is_tested)
                        order by fd.file_name, fd.file_name, prev_run"""  # Functions that changed status from earlier - func, now, before

LAST_CHANGED_TESTS_LIST = """SELECT td.class_name, td.test_Name, 
                                    case td.did_pass when 1 then "Passed" when 0 then "Failed" end as cur_run,
                                    case td2.did_pass when 1 then "Passed" when 0 then "Failed" else "Didn't Exist" end as prev_run
                            FROM tests_details td
                            left join tests_details td2
                            on td2.run_id = td.run_id - 1
                                and td2.class_name = td.class_name
                                and td2.test_Name = td.test_Name
                            where td.run_id in (select max(run_id)
                                              from tests_details) 
                                and (td2.did_pass is NULL or td2.did_pass != td.did_pass)
                            order by td.class_name, td.test_Name, prev_run"""  # Tests that changed status from earlier - test, now, before

"""
----- Html - Coverage Analysis By File page ----
"""

COVERAGE_FILE = """SELECT c.run_id, c.file_name, c.line_rate*100 as percent
                            FROM coverage c
                            where c.run_id in (select distinct run_id
                                            	from coverage
                                             order by run_id desc
                                            	limit {})
                            order by c.file_name desc"""

"""
----- Html - Test Analysis By File ----
"""

TESTS_FILE_TESTED_VS_NOT = """select *
                                from (SELECT fd.run_id, fd.file_name,
                                        Round((CAST(COUNT(case when is_tested = 1 then 1 end) as float)/COUNT(*))*100,2) as test,
                                        Round((CAST(COUNT(case when is_tested = 0 then 1 end) as float)/COUNT(*))*100,2) as notTest
                                FROM functions_details fd
                                group by fd.run_id, fd.file_name)
                                order by run_id desc
                                limit {}"""

TESTS_FILE_HISTORY = """SELECT td.run_id, td.class_name, 
                                       SUM(td.did_pass) as passed,
                                       SUM(case td.did_pass when 1 then 0 when 0 then 1 end) as failed
                                FROM tests_details td
                                GROUP by td.run_id, td.class_name
                                order by td.run_id desc
                                limit {}"""

TESTS_FILE_DID_PASS = """SELECT td.class_name, td.test_Name, 
                                case td.did_pass when 1 then "Passed" when 0 then "Failed" end as cur_run,
                                case td2.did_pass when 1 then "Passed" when 0 then "Failed" else "Didn't Exist" end as prev_run
                        FROM tests_details td
                        left join tests_details td2
                        on td2.run_id = td.run_id - 1
                            and td2.class_name = td.class_name
                            and td2.test_Name = td.test_Name
                        where td.run_id in (select max(run_id)
                                            from tests_details)
                              and (td2.did_pass is NULL or td2.did_pass != td.did_pass)
                        order by td.class_name, td.test_Name, prev_run"""
