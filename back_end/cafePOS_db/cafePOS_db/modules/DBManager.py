# ==========================================
#     DEVELOPER:  J.A. Runnells
#          FILE:  DBManager.py
#        BRANCH: dev
# ==========================================
from sqlite3 import connect, Error, OperationalError
import json


class DBManager:
    """DATABASE MANAGER CLASS"""

    def __init__(self, db=':memory:', data_path=r'./'):
        """
        DBManager Constructor
        :param db: database name
        :param path: 
        """
        self.db = db
        self.data_path = data_path
        self.conn = None
        self.cur = None

    def __repr__(self):
        return f"DBManager({self.db}, {self.data_path})"

    def __str__(self):
        return f"Database={self.db} :=: Path={self.data_path}"

    def create_tables(self, tables):
        """
        Create Tables from .sql file
        :param tables:
        :return:
        """
        with connect(self.db) as self.conn:
            self.cur = self.conn.cursor()
            try:
                with open(tables, 'r') as tbl_file:
                    tbl_sql = tbl_file.read()
                self.cur.executescript(tbl_sql)
                self.conn.commit()
            except Error as err:
                print(f"[ERROR] {err}")
            else:
                print(f"Total changes: {self.conn.total_changes}")
            finally:
                if self.cur:
                    self.cur.close()

    def fetch_tables(self):
        """
        List Tables
        :return:
        """
        query = "SELECT name FROM sqlite_master WHERE type='table';"

        with connect(self.db) as self.conn:
            self.cur = self.conn.cursor()
            try:
                self.cur.execute(query)
                print(self.cur.fetchall())
            except Error as err:
                print(f"[ERROR] {err}")
            else:
                print(self.cur.fetchall())
            finally:
                if self.cur:
                    self.cur.close()

# ===========================================================================================

    def insert_record(self, tbl_name, record):
        """
        Insert Record
        :param tbl_name:
        :param record:
        :return:
        """
        # TODO: implement connection context manager
        try:
            self.connect_db()
            self.create_cursor()
            self.cur.execute(record)
            self.conn.commit()
            self.close_cursor()
        except Error as err:
            print(f"[ERROR] {err}")
        else:
            print(f"Total changes: {self.conn.total_changes}")
        finally:
            if self.conn:
                self.close_connection()

    def insert_records(self, tbl_name, records, is_sql):
        """
        Insert Records
        :param tbl_name:
        :param records:
        :param is_sql:
        :return:
        """
        with connect(self.db) as self.conn:
            self.cur = self.conn.cursor()
            try:
                if is_sql:
                    with open(records, 'r') as rec_file:
                        rec_sql = rec_file.read()
                    self.cur.executescript(rec_sql)
                    # self.conn.commit()
                else:
                    # RECORDS -> NEEDS TO BE PASSED AS A LIST
                    records = [('BK001', 'bkfast', 'Muffin', 'MUFFIN', 2.75),
                               ('HB001', 'bev_hot', 'Coffee', 'COFFEE', 1.99),
                               ('CB001', 'bev_cold', 'Aquafina', 'AQUA H20', 1.00),
                               ('DE001', 'deli', 'Noodle Cup', 'NOODLE CUP', 1.00),
                               ('SN001', 'snack', 'Cookie', 'COOKIE', 1.64),
                               ('CD001', 'condiment', 'Dressing', 'DRESSING', 0.75)]
                    insert_query = f"""
                        BEGIN TRANSACTION;
                        INSERT INTO {tbl_name}(id,category,name,label,price)
                            VALUES (?,?,?,?,?);
                        COMMIT;
                        """
                    self.cur.executemany(insert_query, records)
            except Error as err:
                print(f"[ERROR] {err}")
            else:
                self.conn.commit()
                print(f"Total changes: {self.conn.total_changes}")
            finally:
                if self.cur:
                    self.cur.close()

    def fetch_records(self, tbl_name):
        """
        Fetch Records
        :param tbl_name:
        :return:
        """
        # TODO[FIXME]: MISSING -> try|except|else|finally [Err: sqlite3.OperationalError: no such table]
        # TODO: implement connection context manager
        self.connect_db()
        self.create_cursor()

        query_fetchall = f'SELECT * FROM {tbl_name}'
        self.cur.execute(query_fetchall)
        rows = self.cur.fetchall()

        for row in rows:
            print(row)
            print(f'''
         id: {row[0]}
        cat: {row[1]}
       name: {row[2]}
      label: {row[3]}
      price: $ {row[4]}
    ''')

    def delete_record(self, table, record):
        """
        Delete Record from DB
        :param table: table to remove record from
        :param record: record to remove
        :return:
        """
        # TODO: implement connection context manager
        try:
            self.connect_db()
            self.create_cursor()
            del_query = f'''DELETE FROM {table} WHERE id = ?;'''
            self.cur.execute(del_query, (record,))
        except Error as err:
            print(f"DELETE record [{record}] error [{err}]")
        else:
            self.conn.commit()
            self.close_cursor()
            print(f"Record [{record}] successfully removed!")
        finally:
            if self.conn:
                self.close_connection()

    def drop_tables(self, tables):
        """
        Drop Tables
        :param tables:
        :return:
        """
        # TODO: implement connection context manager
        try:
            self.connect_db()
            self.create_cursor()
            for i, table in enumerate(tables):
                self.cur.execute(f'DROP TABLE IF EXISTS {tables[i]}')
            self.conn.commit()
            self.close_cursor()
        except Error as err:
            print(f"[ERROR] {err}")
        else:
            print(f"Total changes: {self.conn.total_changes}")
        finally:
            if self.conn:
                self.close_connection()

    def dump_db(self):
        """
        Dump Database
        :return:
        """
        out_file = f"/backup/dump_{self.db_name}.sql"
        mode = 'w'

        # TODO: implement connection context manager
        try:
            self.connect_db()
            with open(out_file, mode) as dump:
                for line in self.conn.iterdump():
                    # print(line)
                    dump.write(f"{line}\n")
        except Error as err:
            print(f"[ERROR] {err}")
        else:
            print(f"{out_file} created successfully using mode {mode}")
        finally:
            if self.conn:
                self.close_connection()

    def dump_json(self, tbl_name='items', source_type='sql'):
        """
        Dump Database into JSON file
        :param tbl_name: table name to fetch all records
        :param source_type: source file data type -> 'sql' or 'csv'
        :return:
        """
        query_fetchall = f'SELECT * FROM {tbl_name}'

        if source_type == 'sql':
            # TODO: implement connection context manager
            try:
                self.connect_db()
                self.create_cursor()
                result = self.cur.execute(query_fetchall)
                json_result = [dict(zip([key[0] for key in self.cur.description], row)) for row in result]
            except Error as err:
                print(f"[ERROR] {err}")
            else:
                print(json.dumps({"items": json_result}))
            finally:
                self.close_cursor()
                if self.conn:
                    self.close_connection()

# ===========================================================================================

    def close_db(self, cur=False, conn=False):
        """
        Test Method to encapsulate separated methods
        :param cur: boolean flag triggering self.cur.close()
        :param conn: boolean flag triggering self.conn.close()
        :return:
        """
        if cur:
            self.cur.close()
            print(f" [+] Database CURSOR Closed -> {self.db}")
        elif conn:
            self.conn.close()
            print(f" [+] Database CONNECTION Closed -> {self.db}")
