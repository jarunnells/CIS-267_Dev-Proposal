# ==========================================
#     DEVELOPER:  J.A. Runnells
#          FILE:  app.py
#        BRANCH: main
# ==========================================
from modules.DBManager import DBManager
from modules.Menu import Menu
from modules.helper import Default
import os


def main():
    """ENTRY POINT"""
    
    print(os.getcwd())
    # dbmgr = DBManager(Default.DB_URI, data_path=Default.DATA_PATH)
    m = Menu(
        # dbmgr := DBManager(Default.DB_URI, data_path=Default.DATA_PATH),
        dbmgr := DBManager(),
        data_file=Default.DATA_FILES,
        table_name=Default.TBL_NAME
    )

    show_menu = True
    while show_menu:
        print()
        print(m.display())
        m.switch(choice := input('Selection: ').lower())
        if choice == 'e': show_menu = False
        print()

    if dbmgr.conn: dbmgr.close_db(conn=True)


if __name__ == '__main__': main()
