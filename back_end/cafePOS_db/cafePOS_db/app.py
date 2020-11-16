# ==========================================
#     DEVELOPER:  J.A. Runnells
#          FILE:  app.py
#        BRANCH: dev
# ==========================================
from back_end.cafePOS_db.cafePOS_db.modules.helper import Default
from .modules import DBManager
from .modules import Menu
from .modules import helper


def main():
    """ENTRY POINT"""
    # dbmgr = DBManager(Default.DB_URI, data_path=Default.DATA_PATH)
    m = Menu(
        dbmgr := DBManager(Default.DB_URI, data_path=Default.DATA_PATH),
        data_file=Default.DATA_FILES,
        table_name=Default.TBL_NAME
    )

    show_menu = True
    while show_menu:
        print()
        print(m.display())
        m.switch(choice := input('Selection: ').lower())
        if choice == 'e':
            show_menu = False
        print()

    if dbmgr.conn:
        dbmgr.close_db(conn=True)


if __name__ == '__main__':
    main()
