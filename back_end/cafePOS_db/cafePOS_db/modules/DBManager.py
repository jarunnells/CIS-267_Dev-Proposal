# ==========================================
#     DEVELOPER:  J.A. Runnells
#          FILE:  DBManager.py
#        BRANCH: dev
# ==========================================
from sqlite3 import connect, Error, OperationalError
import json
import sqlite3

from modules.helper import Default


class DBManager:
    """DATABASE MANAGER CLASS"""

    # def __init__(self, db=':memory:', data_path=r'./'):
    def __init__(self, db=Default.DB_MEMORY, data_path=Default.DATA_PATH):
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

    def fetchall_tables(self):
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

    def insert_record(self, record):
        """
        Insert Record
        :param record:
        :return:
        """
        tbl_name = "items"
        create_tbl = f"""BEGIN TRANSACTION; 
        CREATE TABLE IF NOT EXISTS {tbl_name}(
                id TEXT PRIMARY KEY,
                category TEXT NOT NULL,
                name TEXT NOT NULL,
                label TEXT NOT NULL,
                price REAL
            );
        COMMIT;"""
        
        query = f"""
            BEGIN TRANSACTION;
                INSERT INTO {tbl_name}(id,category,name,label,price)
                VALUES (?,?,?,?,?);
            COMMIT;
            """
        
        with connect(self.db) as self.conn:
            self.cur = self.conn.cursor()
            try:
                # record = [('ID_01', 'CAT_01', 'NAME_01', 'LABEL_01', 1.99)]
                record = (item_id := input("ID: "), category := input("Category: "), name := input("Name: "), label := input("Label: "), price := input("Price: "))
                self.cur.execute(create_tbl, (tbl_name,))
                self.cur.execute(query, record)
            except Error as err:
                print(f"[ERROR] {err}")
            else:
                self.conn.commit()
                print(f"Total changes: {self.conn.total_changes}")
            finally:
                if self.cur:
                    self.cur.close()

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
                # TODO: for testing - convert to if sql elif cvs -> manual adds should be single records
                else:
                    # RECORDS -> NEEDS TO BE PASSED AS A LIST
                    records = [
                        ('ID_01', 'CAT_01', 'NAME_01', 'LABEL_01', 1.99),
                        ('ID_02', 'CAT_02', 'NAME_02', 'LABEL_02', 2.99)]
                    insert_query = f"""
                        BEGIN TRANSACTION;
                        INSERT INTO {tbl_name}(id,category,name,label,price)
                            VALUES (?,?,?,?,?);
                        COMMIT;
                        """
                    # self.cur.executemany(insert_query, records) if records.count() > 1 else self.cur.execute(insert_query, records)
                    self.cur.executemany(insert_query, records)
            except Error as err:
                print(f"[ERROR] {err}")
            else:
                self.conn.commit()
                print(f"Total changes: {self.conn.total_changes}")
            finally:
                if self.cur:
                    self.cur.close()

    def fetchall_records(self, tbl_name):
        """
        Fetch All Records
        :param tbl_name:
        :return:
        """
        query = f'SELECT * FROM {tbl_name}'

        with connect(self.db) as self.conn:
            self.cur = self.conn.cursor()
            try:
                self.cur.execute(query)
            except sqlite3.OperationalError as err:
                print(f"[ERROR] {err}")
            except Error as err:
                print(f"[ERROR] {err}")
            else:
                rows = self.cur.fetchall()
                for row in rows:
                    print(row)
                    print(f"\t\t\t\tid: {row[0]}\n\t\t\t   cat: {row[1]}\n\t\t\t  name: {row[2]}\n\t\t\t label: {row[3]}\n\t\t\t price: $ {row[4]}")
            finally:
                if self.cur:
                    self.cur.close()

    def delete_record(self, table, record):
        """
        Delete Record from DB
        :param table: table to remove record from
        :param record: record to remove
        :return:
        """
        query = f"""DELETE FROM ? WHERE id = ?;"""

        with connect(self.db) as self.conn:
            self.cur = self.conn.cursor()
            try:
                self.cur.execute(query, (table, record,))
                self.conn.commit()
            except Error as err:
                print(f"DELETE record [{record}] error [{err}]")
            else:
                print(f"Record [{record}] successfully removed!")
                print(f"Total changes: {self.conn.total_changes}")
            finally:
                if self.cur:
                    self.cur.close()

    def drop_tables(self, tables):
        """
        Drop Tables
        :param tables:
        :return:
        """
        query = f"DROP TABLE IF EXISTS ?"

        with connect(self.db) as self.conn:
            self.cur = self.conn.cursor()
            try:
                for table in tables:
                    self.cur.execute(query, table)
                self.conn.commit()
            except Error as err:
                print(f"[ERROR] {err}")
            else:
                print(f"Total changes: {self.conn.total_changes}")
            finally:
                if self.cur:
                    self.cur.close()

    # TODO: complete implementation and testing
    def dump_db(self):
        """
        Dump Database
        :return:
        """
        out_file = f"/backup/dump_{self.db}.sql"
        mode = 'w'

        with connect(self.db) as self.conn:
            self.cur = self.conn.cursor()
            try:
                with open(out_file, mode) as dump:
                    for line in self.conn.iterdump():
                        # print(line)
                        dump.write(f"{line}\n")
            except Error as err:
                print(f"[ERROR] {err}")
            else:
                print(f"{out_file} created successfully using mode {mode}")
            finally:
                if self.cur:
                    self.cur.close()

    # TODO: complete implementation and testing
    def dump_json(self, tbl_name='items', output_type='sql'):
        """
        Dump Database into JSON file
        :param tbl_name: table name to fetch all records
        :param output_type: source file data type -> 'sql' or 'csv'
        :return:
        """
        query = f"SELECT * FROM {tbl_name}"
        timestamp = 'TEST'
        file_name = f"cafePOS_db-{timestamp}.json"
        file_path = f'/cafePOS_db/cafePOS_db/data/dump_{file_name}'
        mode = 'w'

        if output_type == 'sql':
            with connect(self.db) as self.conn:
                self.cur = self.conn.cursor()
                try:
                    result = self.cur.execute(query)
                    dict_result = [
                        dict(zip([key[0] for key in self.cur.description], row)) for row in result]
                    with open(file_path, mode) as f_json:
                        # MATCH: menuItems.json
                        json.dump(dict_result, f_json)
                        # json.dump(dict_result, f_json, indent=2)
                        # MATCH(ish): menuItems-NEW.json
                        # json.dump({"items": dict_result})
                        # json.dump({"items": dict_result}, indent=2)
                except sqlite3.OperationalError as err:
                    print(f"[ERROR] {err}")
                except Error as err:
                    print(f"[ERROR] {err}")
                else:
                    print(json.dumps({"items": dict_result}))
                    print(json.dumps({"items": dict_result}, indent=2))
                finally:
                    if self.cur:
                        self.cur.close()
        elif output_type == 'csv':
            example_table = [
                (1, 'macOS', 'Catalina', 'YES'),
                (2, 'windows', '10', 'NO'),
                (3, 'linux', 'Mint 20', 'YES'),
                (4, 'iOS', '12', 'YES'),
                (5, 'android', '11', 'NO')
            ]
            columns = ['id', 'operating_sys', 'version', 'updated']
            os_options = [dict(zip(columns, row)) for row in example_table]
            json_result = json.dumps({'OS_Options': os_options}, indent=2)
            # json_result = json.dumps({'OS_Options': os_options})
            # json_result = json.dumps(os_options, indent=2)
            # json_result = json.dumps(os_options)
            print(json_result)

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
