# ==========================================
#     DEVELOPER:  J.A. Runnells
#          FILE:  config.py
#        BRANCH: dev
#
# try:  # Python 2
#     import Tkinter as tk
# except ImportError:  # Python 3
#     import tkinter as tk
#
# ==========================================
# STANDARD LIBRARY IMPORTS
import tkinter as tk
from tkinter import ttk
from typing import (Dict, List, Iterator, Tuple, Any)


FIELD_NAMES: List[str] = ["Item ID", "Category", "Name", "Label", "Price"]

# GUI CONFIG SETTINGS
# TODO: rename 
class Directories:
    """ [summary]

    [extended_summary]
    """
    DATABASE: str = "cafePOS"
    TIMESTAMP: str = "TEST"
    FILENAME: str = f"dump_{DATABASE}_db-{TIMESTAMP}"
    PROJ_ROOT: str = "back_end/cafePOS_db_gui/cafePOS_db_gui/"
    MODE: Tuple[str, ...] = ("w", "wb", "r", "rb")
    PREFIX: Tuple[str, ...] = ("/backup/", "/data/")
    DB_: Dict[str, str] = {
        "prefix": PREFIX[1], 
        "filename": DATABASE, 
        "ext": ".db",
    }
    SQL_: Dict[str, str] = {
        "prefix": PREFIX[0], 
        "filename": FILENAME, 
        "ext": ".sql", 
        "mode": MODE[0],
    }
    JSON_: Dict[str, str] = {
        "prefix": PREFIX[1], 
        "filename": FILENAME, 
        "ext": ".json", 
        "mode": MODE[0],
    }
    CSV_: Dict[str, str] = {
        "prefix": PREFIX[1], 
        "filename": FILENAME, 
        "ext": ".csv", 
        "mode": MODE[0],
    }


class TableNames:
    CAFE_ITEMS: str = "items"
    ACTIVE_TABLE: str = CAFE_ITEMS


# TODO: integrate Messages into per Query as dictionary 
class Messages:
    UPDATE: Dict[str, str] = {
        "title": "CONFIRM UPDATE OPERATION!", 
        "message": f"Please confirm update operation on item:"
        }
    DELETE: Dict[str, str] = {
        "title": "CONFIRM DELETE OPERATION!", 
        "message": f"Please confirm delete operation on item:"
        }
    ERRORS: Dict[str, str] = {
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
    INIT: str = f"BEGIN TRANSACTION; CREATE TABLE IF NOT EXISTS {TableNames.ACTIVE_TABLE} \
        (id TEXT PRIMARY KEY, category TEXT NOT NULL, name TEXT NOT NULL, label TEXT NOT NULL, price REAL NOT NULL); COMMIT;"
    FETCH_ALL: Dict[str, str] = {
        'tables': "SELECT name FROM sqlite_master WHERE type='table'",
        'records': f"SELECT * FROM {TableNames.ACTIVE_TABLE}"
    }
    INSERT: str = f"INSERT INTO {TableNames.ACTIVE_TABLE} VALUES (?, ?, ?, ?, ?)"
    REMOVE: str = f"DELETE FROM {TableNames.ACTIVE_TABLE} WHERE id=?"
    SEARCH: Dict[str, str] = {
        "id_": f"SELECT * FROM {TableNames.ACTIVE_TABLE} WHERE id=?",
        "category_": f"SELECT * FROM {TableNames.ACTIVE_TABLE} WHERE category=?",
        "name_": f"SELECT * FROM {TableNames.ACTIVE_TABLE} WHERE name=?",
        "label_": f"SELECT * FROM {TableNames.ACTIVE_TABLE} WHERE label=?",
        "price_": f"SELECT * FROM {TableNames.ACTIVE_TABLE} WHERE price IN (?)",
    }
    UPDATE: str = f"UPDATE {TableNames.ACTIVE_TABLE} SET id=?, category=?, name=?, label=?, price=? WHERE id=?"
    DROP: str = f"DROP TABLE IF EXISTS {TableNames.ACTIVE_TABLE}"


class Colors:
    LIGHT_STEEL_BLUE: Dict[str, str] = {
        "py_name": "light steel blue", 
        "hex": "#B0C4DE",
    }
    LIGHT_CORAL: Dict[str, str] = {
        "py_name": "light coral", 
        "hex": "#F08080",
    }
    LAVENDER: Dict[str, str] = {
        "py_name": "lavender", 
        "hex": "#E6E6FA",
    }
    ANTIQUE_WHITE: Dict[str, str] = {
        "py_name": "antique white", 
        "hex": "#FAEBD7",
    }
    DARK_SEA_GREEN: Dict[str, str] = {
        "py_name": "dark sea green", 
        "hex": "#8FBC8F",
    }
    STEEL_BLUE = MAIN_ = {
        "py_name": "steel blue", 
        "hex": "#4682B4",
    }
    FIRE_BRICK: Dict[str, str] = {
        "py_name": "'firebrick'", 
        "hex": "#B22222",
    }
    FIRE_BRICK_65: Dict[str, str] = {
        "py_name": "", 
        "hex": "#E26969",
    }
    WHITE_SMOKE: Dict[str, str] = {
        "py_name": "white smoke", 
        "hex": "#F5F5F5",
    }
    GAINSBORO: Dict[str, str] = {
        "py_name": "gainsboro", 
        "hex": "#DCDCDC",
    }
    DARK_RED: Dict[str, str] = {
        "py_name": "", 
        "hex": "#8B0000",
    }


class StylesTtk:
    THEMES: Tuple[str, ...] = ("default", "classic", "clam", "aqua", "alt")


class FrameWidget:
    width = None
    height = None
    relief = None
    bg = None
    borderwidth = None
    background = None
    pady: Dict[str, int] = {"pack": 5, "frame": 10}
    padx: Dict[str, int] = {"pack": 5, "frame": 10}
    side: Dict[str, int] = {"L": tk.LEFT, "R": tk.RIGHT, "T": tk.TOP, "B": tk.BOTTOM}
    fill: str = tk.BOTH
    expand: str = tk.YES
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
    padx: int = 5
    pady: int = 5
    width: int = 12
    padding: Tuple[int, ...] = (padx, pady)
    BTN: Dict[str, Dict[str, Any]] = {
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
    cnf: Dict[str, int] = {
        "width": width,
        "padx": padx,
        "pady": pady
    }
    cnf_grid: Dict[str, int] = {
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
    values: Iterator[str] = ["", "bkfast", "bev_hot", "bev_cold", "deli", "snack", "condiment",]
    search_values: Iterator[str] = ["Search by ...", "item ID", "category", "name", "label", "price"]
    width: int = 18
    # ===== UNUSED ======
    
    # ===================


class ProgressBarWidget():
    pass


class EntryWidget:
    column: int = 1
    width: int = 20
    padx: int = 5
    pady: int = 5
    placeholder: Dict[str, str] = {
        "id_": "Item ID...",
        "category_": "Item Category...",
        "name_": "Item Name...",
        "label_": "Item Label...",
        "price_": "Item Price...",
    }
    cnf_grid: Dict[str, int] = {
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
    bind_seq: str = '<<TreeviewSelect>>'
    columns: Dict[str, List[Any]] = {
        "str": FIELD_NAMES,
        "int": [1,2,3,4,5]
    }
    selectmode: Dict[str, str] = {
        "one": "browse", 
        "many": "extended", 
        "none": "none"
    }
    show: str = "headings"
    HEADINGS: List[str] = columns['str']
    # ===== UNUSED ======
    # displaycolumns = None
    # height = None
    # padding = (pad_left := None, pad_top := None, pad_right := None, pad_bottom := None)
    # ===================


class ListBox:
    bind_seq: str = '<<ListboxSelect>>'
    height: int = 15
    width: int = 45
    border: int = 0
    row: int = 7
    column: int = 0
    columnspan: int = 3
    rowspan: int = 6
    pady: int = 20
    padx: int = 20
    cnf: Dict[str, int] = {
        "height": height,
        "width": width,
        "border": border
    }
    cnf_grid: Dict[str, int] = {
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
    cnf_grid: Dict[str, int] = {
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
    font: Tuple[str, int] = ("bold", 16)
    padx: int = 2
    pady: int = 2
    padding: Tuple[int, ...] = (pad_h := padx, pad_v := pady)
    column: int = 0
    sticky: str = tk.E
    TXT: List[str] = FIELD_NAMES + ["Search (ID)",]
    cnf: Dict[str, int] = {
        "font": font,
        "padx": padx,
        "pady": pady}
    cnf_grid: Dict[str, int] = {
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
