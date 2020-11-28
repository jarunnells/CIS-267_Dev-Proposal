# ==========================================
#     DEVELOPER:  J.A. Runnells
#          FILE:  Menu.py
#        BRANCH: dev
# ==========================================
from sys import exit


class Menu:
    """CONSOLE MENU CLASS"""

    def __init__(self, dbmgr, data_file=None, table_name=None, record=None):
        self.dbmgr = dbmgr
        self.data_file = data_file
        self.record = record
        self.table_name = table_name
        self.clear = lambda: print('\n' * 25)

    def __repr__(self):
        return f"Menu({self.dbmgr}, data_file={self.data_file}, table_name={self.table_name}, record={self.record})"

    def __str__(self):
        """"""
        pass

    @staticmethod
    def display():
        """
        Display Menu Options [StaticMethod]
        :return: textual menu
        """
        return '''
             DATABASE OPTIONS
        ==========================
          [1] Create Tbls SQL
          [2] Fetch All Tables
          [3] Insert Record
          [4] Insert Records SQL
          [5] Fetch All Records
          [6] Delete Record
          [7] Drop Tables
          [8] Dump DB -> SQL
          [9] Dump DB -> JSON
          [E] EXIT
        ==========================
        '''

    # [ ] TODO: switch to ternary operator
    args_list = None

    def switch(self, arg, *args):
        """
        Switch Method
        :param arg: user choice argument
        :param args: additional arguments
        :return: call to appropriate case method
        """
        # [ ] TODO: switch to ternary operator - does SCOPE become issue?
        args_list = args if len(args) > 1 else None
        default = f"INVALID Choice! [{arg}]"
        return getattr(self, f"case_{arg}", lambda: print(default))()
    # [1] Create Tbls SQL
    def case_1(self):
        self.clear()
        self.dbmgr.create_tables(self.data_file['TBLS_SQL'])
    # [2] Fetch All Tables
    def case_2(self):
        self.clear()
        self.dbmgr.fetchall_tables()
    # [3] Insert Record
    def case_3(self):
        self.clear()
        # self.dbmgr.insert_record(self.table_name, self.record)
        self.dbmgr.insert_record(self.record)
    # [4] Insert Records SQL
    def case_4(self):
        self.clear()
        self.dbmgr.insert_records(self.table_name, self.data_file['RECS_SQL'], True)
    # [5] Fetch All Records
    def case_5(self):
        self.clear()
        self.dbmgr.fetchall_records(self.table_name)
    # [6] Delete Record
    def case_6(self):
        self.clear()
        self.dbmgr.delete_record(self.table_name, self.record)
    # [7] Drop Tables
    def case_7(self):
        self.clear()
        self.dbmgr.drop_table('items')
    # [8] Dump DB -> SQL
    def case_8(self):
        self.clear()
        self.dbmgr.dump_db()
    # [9] Dump DB -> JSON
    def case_9(self):
        self.clear()
        self.dbmgr.dump_json()
    # [E] EXIT
    def case_e(self):
        self.clear()
        print("DATABASE UTILITY TERMINATED!")
        exit(0)
