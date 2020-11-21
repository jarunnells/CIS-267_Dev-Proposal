# ==========================================
#     DEVELOPER:  J.A. Runnells
#          FILE:  database.py -> DBManager.py
#        BRANCH: dev
# ==========================================

# STANDARD LIBRARY IMPORTS
from sqlite3 import connect, Error, OperationalError
import json
import sqlite3
# CUSTOM LIBRARY IMPORTS
from modules.config import Query as q_
from modules.config import TableNames as tn_
from modules.config import Directories as d_


def _DEBUG_(choice, cursor=None, connection=None):
    if choice.upper() == "INIT":
        print(cursor.execute(q_.FETCH_ALL_TABLES).fetchall())


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

    # TODO: rename -> fetch_all_records()
    def fetch_all_records(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        self.cur.execute(q_.FETCH_ALL_RECORDS)
        rows = self.cur.fetchall()
        return rows

    # TODO: rename -> insert_record()
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

    # TODO: rename -> remove_record()
    def remove_record(self, id_):
        """[summary]

        Args:
            id_ ([type]): [description]
        """
        self.cur.execute(q_.REMOVE, (id_,))
        self.conn.commit()

    # TODO: rename -> update_record()
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

    # TODO: rename -> search_record_id()
    def search_record_id(self, id_):
        """[summary]

        Args:
            id_ ([type]): [description]

        Returns:
            [type]: [description]
        """
        self.cur.execute(q_.SEARCH, (id_,))
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

    # TODO: finish implementation
    def dump_db_json(self, table_name=None, output_type='json'):
        """Dump database -> JSON

        Args:
            table_name ([type], optional): [description]. Defaults to None.
            output_type (str, optional): [description]. Defaults to 'json'.
        """
        file_path = f"{d_.PROJ_ROOT}{d_.DUMP_JSON['prefix']}{d_.DUMP_JSON['file_name']}{d_.DUMP_JSON['ext']}"
        mode = d_.DUMP_JSON['mode']
                    
        try:
            result = self.cur.execute(q_.FETCH_ALL_RECORDS)
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

    # TODO: finish implementation
    def dump_db_csv(self, table_name=None, output_type='csv'):
        """Dump database -> CSV

        Args:
            table_name ([type], optional): [description]. Defaults to None.
            output_type (str, optional): [description]. Defaults to 'csv'.
        """
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

    # TODO: finish implementation
    def dump_db(self, table_name, output_type):
        """[summary]

        Args:
            table_name ([type]): [description]
            output_type (str, optional): [description]. Defaults to 'sql'.
        """
        if output_type == "sql":
            self.dump_db_sql(table_name, output_type='sql')
        elif output_type == "json":
            self.dump_db_json(table_name, output_type='json')
        elif output_type == "csv":
            self.dump_db_csv(table_name, output_type='csv')
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


# db = Database(':memory:')
# db.insert('BK001', 'bkfast', 'Muffin', 'MUFFIN', 2.75)
# db.insert('HB001', 'bev_hot', 'Coffee', 'COFFEE', 1.99)
# db.insert('CB001', 'bev_cold', 'Aquafina', 'AQUA H20', 1.00)
# db.insert('DE001', 'deli', 'Noodle Cup', 'NOODLE CUP', 1.00)
# db.insert('SN001', 'snack', 'House Cookie', 'HOUSE COOKIE', 1.64)
# db.insert('CD001', 'condiment', 'Dressing', 'DRESSING', 0.75)
