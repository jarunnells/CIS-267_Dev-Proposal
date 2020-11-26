# ==========================================
#     DEVELOPER:  J.A. Runnells
#          FILE:  config.py
#        BRANCH: main
# ==========================================
import tkinter as tk
from tkinter import ttk as ttk

FIELD_NAMES = ["Item ID", "Category", "Name", "Label", "Price"]

# GUI CONFIG SETTINGS
# TODO: rename 
class Directories:
    DATABASE = "cafePOS"
    TIMESTAMP = "TEST"
    FILENAME = f"dump_{DATABASE}_db-{TIMESTAMP}"
    PROJ_ROOT = "back_end/cafePOS_db_gui/cafePOS_db_gui/"
    MODE = ("w", "wb", "r", "rb")
    DB_ = {
        "prefix": "/data/", 
        "filename": DATABASE, 
        "ext": ".db",
    }
    SQL_ = {
        "prefix": "/backup/", 
        "filename": FILENAME, 
        "ext": ".sql", 
        "mode": MODE[0],
    }
    JSON_ = {
        "prefix": "/data/", 
        "filename": FILENAME, 
        "ext": ".json", 
        "mode": MODE[0],
    }
    CSV_ = {
        "prefix": "/data/", 
        "filename": FILENAME, 
        "ext": ".csv", 
        "mode": MODE[0],
    }


class TableNames:
    CAFE_ITEMS = "items"
    ACTIVE_TABLE = CAFE_ITEMS


# TODO: integrate Messages into per Query as dictionary 
class Messages:
    UPDATE = {
        "title": "CONFIRM UPDATE OPERATION!", 
        "message": f"Please confirm update operation on item:"
        }
    DELETE = {
        "title": "CONFIRM DELETE OPERATION!", 
        "message": f"Please confirm delete operation on item:"
        }
    ERRORS = {
        "add_item": {
            "title": "ADD Item Error", 
            "message": "ALL fields required!"
        },
        "update_item": {
            "title": "UPDATE Item Error", 
            "message": "ALL fields required!"
        },
        "remove_item": {
            "title": "REMOVE Item Error", 
            "message": "Click an item row first!"
        }
    }


class Query:
    INIT = f"BEGIN TRANSACTION; CREATE TABLE IF NOT EXISTS {TableNames.ACTIVE_TABLE} \
        (id TEXT PRIMARY KEY, category TEXT NOT NULL, name TEXT NOT NULL, label TEXT NOT NULL, price REAL NOT NULL); COMMIT;"
    FETCH_ALL = {
        'tables': "SELECT name FROM sqlite_master WHERE type='table'",
        'records': f"SELECT * FROM {TableNames.ACTIVE_TABLE}"
    }
    INSERT = f"INSERT INTO {TableNames.ACTIVE_TABLE} VALUES (?, ?, ?, ?, ?)"
    REMOVE = f"DELETE FROM {TableNames.ACTIVE_TABLE} WHERE id=?"
    SEARCH = {
        "id_": f"SELECT * FROM {TableNames.ACTIVE_TABLE} WHERE id=?",
        "category_": f"SELECT * FROM {TableNames.ACTIVE_TABLE} WHERE category=?",
        "name_": f"SELECT * FROM {TableNames.ACTIVE_TABLE} WHERE name=?",
        "label_": f"SELECT * FROM {TableNames.ACTIVE_TABLE} WHERE label=?",
        "price_": f"SELECT * FROM {TableNames.ACTIVE_TABLE} WHERE price IN (?)",
    }
    UPDATE = f"UPDATE {TableNames.ACTIVE_TABLE} SET id=?, category=?, name=?, label=?, price=? WHERE id=?"
    DROP = f"DROP TABLE IF EXISTS {TableNames.ACTIVE_TABLE}"


class Colors:
    LIGHT_STEEL_BLUE = {
        "py_name": "light steel blue", 
        "hex": "#B0C4DE", 
        "rgb": (176, 196, 222),
    }
    LIGHT_CORAL = {
        "py_name": "light coral", 
        "hex": "#F08080", 
        "rgb": (240, 128, 128),
    }
    LAVENDER = {
        "py_name": "lavender", 
        "hex": "#E6E6FA", 
        "rgb": (230, 230, 250),
    }
    ANTIQUE_WHITE = {
        "py_name": "antique white", 
        "hex": "#FAEBD7", 
        "rgb": (250, 235, 215),
    }
    DARK_SEA_GREEN = {
        "py_name": None, 
        "hex": "#8FBC8F", 
        "rgb": (143, 188, 143),
    }
    STEEL_BLUE = MAIN_ = {
        "py_name": None, 
        "hex": "#4682B4", 
        "rgb": (70, 130, 180),
    }
    FIRE_BRICK = {
        "py_name": None, 
        "hex": "#B22222", 
        "rgb": (178, 34, 34),
    }
    FIRE_BRICK_65 = {
        "py_name": None, 
        "hex": "#E26969", 
        "rgb": (226, 105, 105),
    }
    WHITE_SMOKE = {
        "py_name": None, 
        "hex": "#F5F5F5", 
        "rgb": (245, 245, 245),
    }
    GAINSBORO = {
        "py_name": None, 
        "hex": "#DCDCDC", 
        "rgb": (220, 220, 220),
    }
    DARK_RED = {
        "py_name": None, 
        "hex": "#8B0000", 
        "rgb": (139, 0, 0),
    }


class StylesTtk:
    THEMES = ("default", "classic", "clam", "aqua", "alt")


class FrameWidget:
    width = None
    height = None
    relief = None
    bg = None
    borderwidth = None
    background = None
    pady = {"pack": 5, "frame": 10}
    padx = {"pack": 5, "frame": 10}
    side = {"L": tk.LEFT, "R": tk.RIGHT, "T": tk.TOP, "B": tk.BOTTOM}
    fill = tk.BOTH
    expand = tk.YES
    cnf = {}
    cnf_pack = {}
    # ===== UNUSED ======
    # padding = (pad_left := None, pad_top := None, pad_right := None, pad_bottom := None)
    
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
    padding = (padx, pady)
    cnf = {}
    cnf_pack = {}
    # ===== UNUSED ======
    # padding = (pad_left := None, pad_top := None, pad_right := None, pad_bottom := None)
    
    # ===================


class MenuWidget():
    pass


class ButtonWidget:
    padx = 5
    pady = 5
    width = 12
    padding = (padx, pady)
    BTN = {
        "01": {
            "text": "Add Item", 
            "row": 0, 
            "column": 2
        },
        "02": {
            "text": "Remove Item", 
            "row": 0, 
            "column": 3
        },
        "03": {
            "text": "Update Item", 
            "row": 1, 
            "column": 2
        },
        "04": {
            "text": "Clear Input", 
            "row": 1, 
            "column": 3
        },
        "05": { # IMPORT -> CSV, JSON, SQL
            "text": "Import DB", 
            "row": 2, 
            "column": 2
        },
        "06": { # EXPORT -> CSV, JSON, SQL
            "text": "Export DB", 
            "row": 2, 
            "column": 3
        },
        "07": { # SEARCH BY -> table fields
            "text": "Search By...", 
            "row": 3, 
            "column": 2, 
            "columnspan": 2
        },
        "08": {
            "text": "Search", 
            "row": 4, 
            "column": 2
        },
        "09": {
            "text": "Reload", 
            "row": 4, 
            "column": 3
        }
    }
    cnf = {
        "width": width,
        "padx": padx,
        "pady": pady
    }
    cnf_grid = {
        "padx": padx,
        "pady": pady
    }
    # ===== UNUSED ======
    # padding = (pad_left := None, pad_top := None, pad_right := None, pad_bottom := None)
    # bg = None
    # text = None
    # command = None
    # height = None
    # font = None        
    # row = None
    # column = None
    # ===================


class MenuButtonWidget():
    pass


class ComboboxWidget():
    # STANDARD OPTIONS
    cursor = None
    placehoder = None
    style = None
    tackefocus = None
    # WIDGET OPTIONS
    exportselection = None
    justify = None
    height = None
    postcommand = None
    state = None
    textvariable = None
    values = ["", "bkfast", "bev_hot", "bev_cold", "deli", "snack", "condiment",]
    width = 18
    # ===== UNUSED ======
    
    # ===================


class ProgressBarWidget():
    pass


class EntryWidget:
    column = 1
    width = 20
    padx = 5
    pady = 5
    placeholder = {
        "id_": "Item ID...",
        "category_": "Item Category...",
        "name_": "Item Name...",
        "label_": "Item Label...",
        "price_": "Item Price...",
    }
    cnf_grid = {
        "column": column,
        "padx": padx,
        "pady": pady
    }
    # ===== UNUSED ======
    # padding = (pad_left := None, pad_top := None, pad_right := None, pad_bottom := None)
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
    columns = {
        "str": FIELD_NAMES,
        "int": (1,2,3,4,5)
    }
    selectmode = {
        "one": "browse", 
        "many": "extended", 
        "none": "none"
    }
    show = "headings"
    HEADINGS = columns['str']
    # ===== UNUSED ======
    # displaycolumns = None
    # height = None
    # padding = (pad_left := None, pad_top := None, pad_right := None, pad_bottom := None)
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


class ScrollbarWidget:    
    row = 7
    column = 3
    sticky = tk.W
    cnf = {}
    cnf_grid = {
        "row": row, 
        "column": column, 
        "sticky": sticky
    }
    # ===== UNUSED ======
    # command = None
    # name = None
    # orient = None
    # ===================


class LabelField:        
    font = ("bold", 16)
    padx = 2
    pady = 2
    padding = (pad_h := padx, pad_v := pady)
    column = 0
    sticky = tk.E
    TXT = FIELD_NAMES + ["Search (ID)",]
    cnf = {
        "font": font,
        "padx": padx,
        "pady": pady}
    cnf_grid = {
        "column": column,
        "sticky": sticky
    }
    # ===== UNUSED ======
    # padding = (pad_left := None, pad_top := None, pad_right := None, pad_bottom := None)
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
