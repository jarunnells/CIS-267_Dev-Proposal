# ==========================================
#     DEVELOPER:  J.A. Runnells
#          FILE:  database.py -> DBManager.py
#        BRANCH: dev
# ==========================================

# STANDARD LIBRARY IMPORTS
from sqlite3 import connect, Error, OperationalError
import json
import csv
import sqlite3
import logging
# CUSTOM LIBRARY IMPORTS
from modules.config import Query as q_
from modules.config import TableNames as tn_
from modules.config import Directories as d_


def _DEBUG_(choice, cursor=None, connection=None):
    if choice.upper() == "INIT":
        print(cursor.execute(q_.FETCH_ALL['tables']).fetchall())


class Database:
    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.cur = self.conn.cursor()
        self.cur.executescript(q_.INIT)

        # DEBUG :=: REMOVE =========================
        _DEBUG_(choice="init", cursor=self.cur)
        # ==========================================

    def __repr__(self):
        return f"Database({self.db})"

    def __str__(self):
        conn_status = "CONNECTED" if self.conn else "DISCONNECTED"
        return f"Database={self.db} :=: Connection={conn_status}"

    def fetch_all_records(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        self.cur.execute(q_.FETCH_ALL['records'])
        rows = self.cur.fetchall()
        return rows

    def insert_record(self, id_, category_, name_, label_, price_):
        """[summary]

        Args:
            id_ ([type]): [description]
            category_ ([type]): [description]
            name_ ([type]): [description]
            label_ ([type]): [description]
            price_ ([type]): [description]
        """
        self.cur.execute(q_.INSERT, (id_, category_, name_, label_, price_))
        self.conn.commit()

    def remove_record(self, id_):
        """[summary]

        Args:
            id_ ([type]): [description]
        """
        self.cur.execute(q_.REMOVE, (id_,))
        self.conn.commit()

    def update_record(self, id_, category_, name_, label_, price_):
        """[summary]

        Args:
            id_ ([type]): [description]
            category_ ([type]): [description]
            name_ ([type]): [description]
            label_ ([type]): [description]
            price_ ([type]): [description]
        """
        self.cur.execute(
            q_.UPDATE, (id_, category_, name_, label_, price_, id_)
        )
        self.conn.commit()

    def search_record_id(self, id_):
        """[summary]

        Args:
            id_ ([type]): [description]

        Returns:
            [type]: [description]
        """
        self.cur.execute(q_.SEARCH['id_'], (id_,))
        rows = self.cur.fetchall()
        return rows

    # TODO: finish implementation
    def create_tables(self, tables):
        """[summary]

        Args:
            table_name ([type]): [description]
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
    def drop_table(self, table=None, tables=None, drop_all=False):
        """[summary]

        Args:
            table_name ([type]): [description]
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
    def dump_db_sql(self, table_name, output_type='sql'):
        """Dump database -> SQL

        Args:
            table_name ([type]): [description]
            output_type (str, optional): [description]. Defaults to 'sql'.
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
    def dump_db_json(self, table_name=None, output_type='json'):
        """Dump database -> JSON

        Args:
            table_name ([type], optional): [description]. Defaults to None.
            output_type (str, optional): [description]. Defaults to 'json'.
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
        except sqlite3.OperationalError as err:
            print(f"[ERROR] {err}")
        except Error as err:
            print(f"[ERROR] {err}")
        # else:
        #     print(json.dumps({"items": dict_result}))
        #     print(json.dumps({"items": dict_result}, indent=2))

    # TODO: finish implementation
    def dump_db_csv(self, table_name=None, output_type='csv'):
        """Dump database -> CSV

        Args:
            table_name ([type], optional): [description]. Defaults to None.
            output_type (str, optional): [description]. Defaults to 'csv'.
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
        except sqlite3.OperationalError as err:
            print(f"[ERROR] {err}")
        except Error as err:
            print(f"[ERROR] {err}")
        except IOError:
            logging.exception('')

    # TODO: finish implementation
    def dump_db(self, table_name, output_type):
        """[summary]

        Args:
            table_name ([type]): [description]
            output_type (str, optional): [description]. Defaults to 'sql'.
        """
        try:
            result = self.cur.execute(q_.FETCH_ALL['records'])            
        except sqlite3.OperationalError as err:
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
    def connect_table(self, table_name):
        """[summary]

        Args:
            table_name ([type]): [description]
        """
        pass

    def __del__(self):
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
