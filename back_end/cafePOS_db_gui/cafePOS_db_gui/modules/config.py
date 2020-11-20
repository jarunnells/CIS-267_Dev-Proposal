# ==========================================
#     DEVELOPER:  J.A. Runnells
#          FILE:  config.py
#        BRANCH: dev
# ==========================================
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
    
# GUI CONFIG SETTINGS

# TODO: rename 
class Directories:
    TIMESTAMP = "TEST"
    FILE_NAME = f"dump_cafePOS_db-{TIMESTAMP}"
    PROJ_ROOT = "/cafePOS_db/cafePOS_db"
    DUMP_SQL = {"prefix": "/backup/", "file_name": FILE_NAME, "ext": ".sql", "mode": "w"}
    DUMP_JSON = {"prefix": "/data/", "file_name": FILE_NAME, "ext": ".json", "mode": "w"}
    DUMP_CSV = {"prefix": "/data/", "file_name": FILE_NAME, "ext": ".csv", "mode": "w"}

class TableNames:
    CAFE_ITEMS = "items"
    ACTIVE_TABLE = CAFE_ITEMS

# TODO: integrate Messages into per Query as dictionary 
class Messages:
    UPDATE = {"title": "CONFIRM UPDATE OPERATION!", "message": f"Please confirm update operation on item:"}
    DELETE = {"title": "CONFIRM DELETE OPERATION!", "message": f"Please confirm delete operation on item:"}

class Query:
    INIT = f"BEGIN TRANSACTION; CREATE TABLE IF NOT EXISTS {TableNames.ACTIVE_TABLE} (id TEXT PRIMARY KEY, category TEXT NOT NULL, name TEXT NOT NULL, label TEXT NOT NULL, price REAL NOT NULL); COMMIT;"
    FETCH_ALL_TABLES = "SELECT name FROM sqlite_master WHERE type='table'"
    FETCH_ALL_RECORDS = f"SELECT * FROM {TableNames.ACTIVE_TABLE}"
    INSERT = f"INSERT INTO {TableNames.ACTIVE_TABLE} VALUES (?, ?, ?, ?, ?)"
    REMOVE = f"DELETE FROM {TableNames.ACTIVE_TABLE} WHERE id=?"
    SEARCH = f"SELECT * FROM {TableNames.ACTIVE_TABLE} WHERE id=?"
    UPDATE = f"UPDATE {TableNames.ACTIVE_TABLE} SET id=?, category=?, name=?, label=?, price=? WHERE id=?"
    DROP = f"DROP TABLE IF EXISTS {TableNames.ACTIVE_TABLE}"

class MessageBoxWidget:
    ERRORS = {
        "add_item": {"title": "REQUIRED!", "message": "ALL fields required."}
    }

class Colors:
    LIGHT_STEEL_BLUE = {"py_name": "light steel blue", "hex": "#B0C4DE", "rgb": (176, 196, 222)}
    LIGHT_CORAL = {"py_name": "light coral", "hex": "#F08080", "rgb": (240, 128, 128)}
    LAVENDER = {"py_name": "lavender", "hex": "#E6E6FA", "rgb": (230, 230, 250)}
    ANTIQUE_WHITE = {"py_name": "antique white", "hex": "#FAEBD7", "rgb": (250, 235, 215)}

class FrameWidget:
    width = None
    height = None
    relief = None
    bg = None
    borderwidth = None
    background = None
    pady = None
    padx = None
    side = None
    fill = None
    cnf = {}
    cnf_pack = {}
    # ===== UNUSED ======
    
    # ===================

class LabelFrameWidget:
    text = None
    width = None
    height = None
    relief = None
    bg = None
    borderwidth = None
    pady = None
    padx = None
    cnf = {}
    cnf_pack = {}
    # ===== UNUSED ======
    
    # ===================

class ButtonWidget:
    padx = 0
    pady = 0
    width = 12
    TXT = [
        "Add Item",
        "Remove Item",
        "Update Item",
        "Clear Input",
        "Import DB",    # IMPORT -> CSV, JSON
        "Export DB",    # EXPORT -> CSV, JSON
        "Admin",        # ADMIN -> CREATE_TBL, DROP_TBL, DUMP:=backup.sql, DUMP:=items.json
        "BLANK",        #
        "BLANK",        #
        "BLANK",        #
        "Search",
        "Reload"
    ]
    cnf = {"width": width}
    cnf_grid = {
        "padx": padx,
        "pady": pady
    }
    # ===== UNUSED ======
    # bg = None
    # text = None
    # command = None
    # height = None
    # font = None        
    # row = None
    # column = None
    # ===================

class InputFieldWidget:
    column = 1
    cnf_grid = {"column": column}
    # ===== UNUSED ======
    # width = None
    # textvariable = None
    # row = None
    # bg = None
    # font = None
    # justify = None
    # relief = None
    # state = None
    # cnf = {}
    # ===================

class TreeViewWidget:
    bind_seq = '<<TreeviewSelect>>'
    columns = (1,2,3,4,5)
    selectmode = "browse"
    show = "headings"
    HEADINGS = ["Item ID", "Category", "Name", "Label", "Price"]
    # ===== UNUSED ======
    # displaycolumns = None
    # height = None
    # padding = (None, None, None,  None)
    # ===================

class ListBox:
    bind_seq = '<<ListboxSelect>>'
    height = 15
    width = 45
    border = 0
    row = 7
    column = 0
    columnspan = 3
    rowspan = 6
    pady = 20
    padx = 20
    cnf = {
        "height": height,
        "width": width,
        "border": border
    }
    cnf_grid = {
        "row": row,
        "column": column,
        "columnspan": columnspan,
        "rowspan": rowspan,
        "pady": pady,
        "padx": padx
    }
    # ===== UNUSED ======
    # bg = None
    # bd = None
    # cursor = None
    # font = None
    # fg = None
    # highlightcolor = None
    # highlightthickness = None
    # relief = None
    # selectbackground = None
    # selectmode = None  # [default=BROWSE, SINGLE, MULTIPLE, EXTENDED]
    # xscrollcommand = None
    # yscrollcommand = None
    # exportselection = None
    # ===================

class BarScroll:    
    row = 7
    column = 3
    sticky = tk.W
    cnf = {}
    cnf_grid = {"row": row, "column": column, "sticky": sticky}
    # ===== UNUSED ======
    # command = None
    # name = None
    # orient = None
    # ===================

class LabelField:        
    font = ("bold", 14)
    padx = 0
    pady = 0        
    column = 0
    sticky = tk.E
    TXT = ["Item ID", "Category", "Name", "POS Label", "Price", "Search (ID)"]
    cnf = {
        "font": font,
        "padx": padx,
        "pady": pady}
    cnf_grid = {
        "column": column,
        "sticky": sticky
    }
    # ===== UNUSED ======
    # text = None
    # width = None
    # textvariable = None
    # bg = None
    # row = None
    # sticky = None
    # justify = None
    # relief = None
    # image = None
    # anchor = None
    # ===================

class VarString:
    # ===== UNUSED ======
    # value = None
    # name = None
    # ===================
    pass
