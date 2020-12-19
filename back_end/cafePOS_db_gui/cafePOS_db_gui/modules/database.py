# ==========================================
#     DEVELOPER:  J.A. Runnells
#          FILE:  database.py -> DBManager.py
#        BRANCH: dev
# ==========================================

# STANDARD LIBRARY IMPORTS
import csv
import json
import logging
import sqlite3 as sql3
from sqlite3 import (connect, Error, OperationalError)
from typing import (Any, List, Iterator, Union)

# THIRD PARTY IMPORTS

# LOCAL APPLICATION IMPORTS
'''
from config import (
    Directories as d_, TableNames as tn_, Query as q_
)
'''
from modules.config import (
    Directories as d_, TableNames as tn_, Query as q_
)


def _DEBUG_(choice: str, cursor: sql3.Cursor = None, connection: sql3.Connection = None) -> None:
    """_DEBUG_ [summary]

    [extended_summary]

    :param choice: [description]
    :type choice: str
    :param cursor: [description], defaults to None
    :type cursor: sql3.Cursor, optional
    :param connection: [description], defaults to None
    :type connection: sql3.Connection, optional
    """
    if choice.upper() == "INIT":
        print(cursor.execute(q_.FETCH_ALL['tables']).fetchall())


class Database:
    def __init__(self, db: str) -> None:
        self.db = db
        self.conn: sql3.Connection = sql3.connect(self.db)
        self.cur: sql3.Cursor = self.conn.cursor()
        self.cur.executescript(q_.INIT)

        # DEBUG :=: REMOVE =========================
        _DEBUG_(choice="init", cursor=self.cur)
        # ==========================================

    def __repr__(self) -> str:
        return f"Database({self.db})"

    def __str__(self) -> str:
        conn_status = "CONNECTED" if self.conn else "DISCONNECTED"
        return f"Database={self.db} :=: Connection={conn_status}"

    def fetch_all_records(self) -> List[Union[str, str, str, str, float]]:
        """fetch_all_records [summary]

        [extended_summary]

        :return: [description]
        :rtype: List[Union[str, str, str, str, float]]
        """
        self.cur.execute(q_.FETCH_ALL['records'])
        rows = self.cur.fetchall()
        return rows

    def insert_record(self, id_: str, category_: str, name_: str, label_: str, price_: float) -> None:
        """insert_record [summary]

        [extended_summary]

        :param id_: [description]
        :type id_: str
        :param category_: [description]
        :type category_: str
        :param name_: [description]
        :type name_: str
        :param label_: [description]
        :type label_: str
        :param price_: [description]
        :type price_: float
        """
        self.cur.execute(q_.INSERT, (id_, category_, name_, label_, price_))
        self.conn.commit()

    def remove_record(self, id_: str) -> None:
        """remove_record [summary]

        [extended_summary]

        :param id_: [description]
        :type id_: str
        """
        self.cur.execute(q_.REMOVE, (id_,))
        self.conn.commit()

    def update_record(self, id_: str, category_: str, name_: str, label_: str, price_: float) -> None:
        """update_record [summary]

        [extended_summary]

        :param id_: [description]
        :type id_: str
        :param category_: [description]
        :type category_: str
        :param name_: [description]
        :type name_: str
        :param label_: [description]
        :type label_: str
        :param price_: [description]
        :type price_: float
        """
        self.cur.execute(
            q_.UPDATE, (id_, category_, name_, label_, price_, id_)
        )
        self.conn.commit()

    def search_record_id(self, id_: str) -> List[Union[str, str, str, str, float]]:
        """search_record_id [summary]

        [extended_summary]

        :param id_: [description]
        :type id_: str
        :return: [description]
        :rtype: List[Union[str, str, str, str, float]]
        """
        self.cur.execute(q_.SEARCH['id_'], (id_,))
        rows = self.cur.fetchall()
        return rows

    # TODO: finish implementation
    def create_tables(self, tables: str) -> None:
        """create_tables [summary]

        [extended_summary]

        :param tables: [description]
        :type tables: str
        """
        try:
            with open(tables, 'r') as tbl_file:
                tbl_sql = tbl_file.read()
            self.cur.executescript(tbl_sql)
            self.conn.commit()
        except Error as err:
            print(f"[ERROR] {err}")
        else:
            print(f"Total changes: {self.conn.total_changes}")

    # TODO: finish implementation
    def drop_table(self, table_name: str = None, tables: Iterator[str] = None, drop_all: bool = False) -> None:
        """drop_table [summary]

        [extended_summary]

        :param table_name: [description], defaults to None
        :type table_name: str, optional
        :param tables: [description], defaults to None
        :type tables: Iterator[str], optional
        :param drop_all: [description], defaults to False
        :type drop_all: bool, optional
        """
        if not drop_all:
            try:
                self.cur.execute(q_.DROP)
            except Error as err:
                print(f"[ERROR] {err}")
            else:
                self.conn.commit()
                print(f"Total changes: {self.conn.total_changes}")
        else:
            try:
                for _ in tables:
                    self.cur.execute(q_.DROP)                
            except Error as err:
                print(f"[ERROR] {err}")
            else:
                self.conn.commit()
                print(f"Total changes: {self.conn.total_changes}")

    # TODO: finish implementation
    def dump_db_sql(self, table_name: str, output_type: str = 'sql') -> None:
        """dump_db_sql >> Dump database -> SQL

        [extended_summary]

        :param table_name: [description]
        :type table_name: str
        :param output_type: [description], defaults to 'sql'
        :type output_type: str, optional
        """
        out_file = f"{d_.PROJ_ROOT}{d_.SQL_['prefix']}{d_.SQL_['filename']}{d_.SQL_['ext']}"
        mode = d_.SQL_['mode']

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

    # TODO: finish implementation
    def dump_db_json(self, table_name: str = None, output_type: str = 'json') -> None:
        """dump_db_json >> Dump database -> JSON

        [extended_summary]

        :param table_name: [description], defaults to None
        :type table_name: str, optional
        :param output_type: [description], defaults to 'json'
        :type output_type: str, optional
        """
        file_path = f"{d_.PROJ_ROOT}{d_.JSON_['prefix']}{d_.JSON_['filename']}{d_.JSON_['ext']}"
        mode = d_.JSON_['mode']
                    
        try:
            result = self.cur.execute(q_.FETCH_ALL['records'])
            dict_result = [
                dict(zip([key[0] for key in self.cur.description], row)) for row in result]
            with open(file_path, mode) as f_json:
                # MATCH: menuItems.json
                json.dump(dict_result, f_json)
                # json.dump(dict_result, f_json, indent=2)
                # MATCH(ish): menuItems-NEW.json
                # json.dump({"items": dict_result})
                # json.dump({"items": dict_result}, indent=2)
        except sql3.OperationalError as err:
            print(f"[ERROR] {err}")
        except Error as err:
            print(f"[ERROR] {err}")
        # else:
        #     print(json.dumps({"items": dict_result}))
        #     print(json.dumps({"items": dict_result}, indent=2))

    # TODO: finish implementation
    def dump_db_csv(self, table_name: str = None, output_type: str = 'csv') -> None:
        """dump_db_csv >> Dump database -> CSV

        [extended_summary]

        :param table_name: [description], defaults to None
        :type table_name: str, optional
        :param output_type: [description], defaults to 'csv'
        :type output_type: str, optional
        """
        file_path = f"{d_.PROJ_ROOT}{d_.CSV_['prefix']}{d_.CSV_['filename']}{d_.CSV_['ext']}"
        mode = d_.CSV_['mode']
        delimiter = ','
        quoting = csv.QUOTE_MINIMAL
        
        try:
            result = self.cur.execute(q_.FETCH_ALL['records'])
            with open(file_path, mode) as f_csv:
                result_csv = csv.writer(f_csv, delimiter, quoting)
                # HEADER ROW
                result_csv.writerow(row=[desc[0] for desc in self.cur.description])
                # DATA ROWS
                result_csv.writerows(rows=result)
        except sql3.OperationalError as err:
            print(f"[ERROR] {err}")
        except Error as err:
            print(f"[ERROR] {err}")
        except IOError:
            logging.exception('')

    # TODO: finish implementation
    def dump_db(self, table_name: str, output_type: str) -> None:
        """dump_db [summary]

        [extended_summary]

        :param table_name: [description]
        :type table_name: str
        :param output_type: [description]
        :type output_type: str
        """
        try:
            result = self.cur.execute(q_.FETCH_ALL['records'])            
        except sql3.OperationalError as err:
            print(f"[ERROR] {err}")
        except Error as err:
            print(f"[ERROR] {err}")
        
        if output_type == "sql":
            # self.dump_db_sql(table_name, output_type='sql')
            print("DUMP -> SQL requested....")
            
            # self.dump_db_sql(table_name, output_type='sql', result)
            # self.dump_db_sql(table_name, output_type='sql', result=self.cur.execute(q_.FETCH_ALL['records']))
        elif output_type == "json":
            # self.dump_db_json(table_name, output_type='json')
            print("DUMP -> JSON requested....")
            
            # self.dump_db_json(table_name, output_type='json', result)
            # self.dump_db_json(table_name, output_type='json', result=self.cur.execute(q_.FETCH_ALL['records']))
        elif output_type == "csv":
            # self.dump_db_csv(table_name, output_type='csv')
            print("DUMP -> CSV requested....")
            
            # self.dump_db_csv(table_name, output_type='csv', result)
            # self.dump_db_csv(table_name, output_type='csv', result=self.cur.execute(q_.FETCH_ALL['records']))
        else:
            print("[ERROR] File type not supported! Try again! (Supported := sql, json, csv)")

    # TODO: future implementation
    def connect_table(self, table_name: str) -> None:
        """connect_table [summary]

        [extended_summary]

        :param table_name: [description]
        :type table_name: str
        """
        pass

    def __del__(self) -> None:
        if self.cur:
            self.cur.close()
            print("CURSOR CLOSED!")
        if self.conn:
            self.conn.close()
            print("DATABASE CLOSED!")


# db.insert_record('BK001', 'bkfast', 'Muffin', 'MUFFIN', 2.75)
# db.insert_record('BK002', 'bkfast', 'House Bagel', 'BAGEL', 3.99)
# db.insert_record('BK003', 'bkfast', 'Breakfast Burrito', 'B-BURRITO', 2.80)
# db.insert_record('BK004', 'bkfast', 'Breakfast Sandwich', 'B-SAND', 2.80)
# db.insert_record('BK005', 'bkfast', 'Bagel', 'BAGEL', 1.50)
# db.insert_record('BK006', 'bkfast', 'Yogurt', 'YOGURT', 2.30)
# db.insert_record('HB001', 'bev_hot', 'Coffee', 'COFFEE', 1.99)
# db.insert_record('HB002', 'bev_hot', 'Hot Tea', 'HOT TEA', 1.99)
# db.insert_record('HB003', 'bev_hot', 'Hot Cocoa', 'COCOA', 1.99)
# db.insert_record('CB001', 'bev_cold', 'Aquafina', 'AQUAFINA', 1.00)
# db.insert_record('CB002', 'bev_cold', 'Life Water', 'LIFE H20', 1.87)
# db.insert_record('CB003', 'bev_cold', 'Sobe', 'SOBE', 2.34)
# db.insert_record('CB004', 'bev_cold', '5hr Energy', '5 HOUR', 2.80)
# db.insert_record('CB005', 'bev_cold', 'Rockstar', 'ROCKSTAR', 2.80)
# db.insert_record('CB006', 'bev_cold', 'Milk', 'MILK', 1.87)
# db.insert_record('CB007', 'bev_cold', 'Chocolate Milk', 'CHOC MILK', 1.87)
# db.insert_record('CB008', 'bev_cold', 'Juice', 'JUICE', 1.87)
# db.insert_record('DE001', 'deli', 'Noodle Cup', 'NOODLE CUP', 1.00)
# db.insert_record('DE002', 'deli', 'Soup', 'SOUP', 2.80)
# db.insert_record('DE003', 'deli', 'Small Salad', 'SM SALAD', 2.10)
# db.insert_record('DE004', 'deli', 'Large Salad', 'LG SALAD', 5.00)
# db.insert_record('DE005', 'deli', 'Deli Sand', 'DELI SAND', 4.44)
# db.insert_record('DE006', 'deli', 'Fresh Whole Fruit', 'FRESH FRUIT', 1.00)
# db.insert_record('DE007', 'deli', 'Fruit Cup', 'FRUIT CUP', 2.30)
# db.insert_record('DE008', 'deli', 'Hummus', 'HUMMUS', 2.69)
# db.insert_record('DE009', 'deli', 'Guacamole', 'GUAC', 2.69)
# db.insert_record('DE010', 'deli', 'String Cheese', 'STRING CHZ', 0.75)
# db.insert_record('DE011', 'deli', 'Veggies Snack Pack', 'VEGGIES', 1.49)
# db.insert_record('DE012', 'deli', 'Sargento Snack Pack', 'SARGENTO', 1.49)
# db.insert_record('SN002', 'snack', 'Chips', 'CHIPS', 0.65)
# db.insert_record('SN003', 'snack', 'House Baked Cookie', 'HOUSE COOKIE', 1.64)
# db.insert_record('SN004', 'snack', 'Oreo Cookie', 'OREO COOKIES', 0.75)
# db.insert_record('SN005', 'snack', 'M&M Cookie', 'M&M COOKIE', 0.75)
# db.insert_record('SN006', 'snack', 'Chips Ahoy', 'CHIPS AHOY', 0.75)
# db.insert_record('SN007', 'snack', 'Rice Krispy', 'RICE KRISPY', 0.75)
# db.insert_record('SN008', 'snack', 'Candy', 'CANDY', 0.75)
# db.insert_record('SN009', 'snack', 'Kind Bar', 'KIND BAR', 2.49)
# db.insert_record('SN010', 'snack', 'Oreo Pie', 'OREO PIE', 2.99)
# db.insert_record('CD001', 'condiment', 'Salsa', 'SALSA', 0.00)
# db.insert_record('CD002', 'condiment', 'Plain Cream Cheese', 'PLAIN CRM CHZ', 0.75)
# db.insert_record('CD003', 'condiment', 'House Cream Cheese', 'HOUSE CRM CHZ', 0.75)
# db.insert_record('CD004', 'condiment', 'Granola', 'GRANOLA', 0.50)
# db.insert_record('CD005', 'condiment', 'Crackers', 'CRACKERS', 0.00)
# db.insert_record('CD006', 'condiment', 'Dressing', 'DRESSING', 0.75)
