# ==========================================
#     DEVELOPER:  J.A. Runnells
#          FILE:  helper.py
#        BRANCH: dev
# ==========================================
from subprocess import call
from os import system, name


TABLE_ITEMS_BLUEPRINT = [
    ['id', 'TEXT', 'PRIMARY KEY'],
    ['category', 'TEXT NOT NULL'],
    ['name', 'TEXT NOT NULL'],
    ['label', 'TEXT NOT NULL'],
    ['price', 'REAL']
]

# TODO: complete implementation
class Default():
    DEVELOPER = "J.A. Runnells"
    VERSION = 1.0
    PROGRAM_NAME = "helper.py"
    DB_MEMORY = r':memory:'
    DATA_PATH = r'./back_end/cafePOS_db/cafePOS_db/data/'
    DB_NAME = r'cafePOS'
    TBL_NAME = r'items'
    EXT_DB = r'db'
    EXT_SQL = r'sqlite3'
    DB_URI = DB_NAME
    DATA_FILES = {
        'TBLS_SQL': r'./back_end/cafePOS_db/cafePOS_db/data/sqlite_script_tables.sql', 
        'RECS_SQL': r'./back_end/cafePOS_db/cafePOS_db/data/sqlite_script_records.sql'
    }
    # TBLS_SQL = r'./back_end/cafePOS_db/cafePOS_db/data/sqlite_script_tables.sql'
    # RECS_SQL = r'./back_end/cafePOS_db/cafePOS_db/data/sqlite_script_records.sql'

# TODO: complete implementation -- under development -> NOT TESTED
@staticmethod
def clear(os_name=None):
    if os_name == 'os': _ = system('cls' if name == 'nt' else 'clear')
    elif os_name == 'sub': _ = call('cls' if name == 'nt' else 'clear', shell=True)
    else: print('\n' * 25)