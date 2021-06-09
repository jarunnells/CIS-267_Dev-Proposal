#!/usr/bin/python3
# ==========================================
#     DEVELOPER:  J.A. Runnells
#          FILE:  app_gui.py
#        BRANCH:  dev
# ==========================================

# STANDARD LIBRARY IMPORTS
import tkinter as tk
import tkinter.font as tk_font
from tkinter import (ttk, messagebox)

# THIRD PARTY IMPORTS

# LOCAL IMPORTS
'''
from sys import path
print(path)
path.append('modules')
from config import (
    Directories as d_, Messages as m_, Colors as c_,
    FrameWidget as f_, TreeViewWidget as tv_,
    ButtonWidget as b_, EntryWidget as e_,
    ComboboxWidget as cb_, LabelField as lf_, StylesTtk as st_,
)
from database import Database
'''
from modules.config import (
    Directories as d_, Messages as m_, Colors as c_,
    FrameWidget as f_, TreeViewWidget as tv_,
    ButtonWidget as b_, EntryWidget as e_,
    ComboboxWidget as cb_, LabelField as lf_, StylesTtk as st_,
)
from modules.database import Database

# db = Database(":memory:")
db = Database(f"{d_.PROJ_ROOT}{d_.DB_['prefix']}{d_.DB_['filename']}{d_.DB_['ext']}")


# TODO: FINISH IMPLEMENTATION -> config.py
class GUI(tk.Frame):

    def __init__(self, master, app_width, app_height, x, y):
        # super(GUI, self).__init__(master)
        super().__init__(master)
        self.master = master
        master.title("Cafe POS Database Management")
        master.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        master.resizable(width=False, height=False)
        master['bg'] = c_.MAIN_['hex']
        self.initialize_UI()

    def initialize_UI(self):
        """initialize_UI [summary]

        [extended_summary]
        """
        self.selected_item_values = 0
        self.create_frames()
        self.create_menubar()
        self.create_labels_entries_combo()
        self.create_buttons()
        self.create_treeview()
        self.create_styles()
        self.populate_tree()

    def create_styles(self):
        """create_styles [summary]

        [extended_summary]
        """
        self.style = ttk.Style()
        self.style.theme_use(st_.THEMES[2])
        self.style.configure(
            "TLabel",
            background=c_.MAIN_['hex'],
            foreground=c_.WHITE_SMOKE['hex'],
        )
        self.style.configure(
            "TEntry",
            padding=(5,),
        )
        self.style.configure(
            "TCombobox",
            padding=(5,),
        )
        self.style.configure(
            "Search.TCombobox",
            justify=tk.CENTER,
        )
        self.style.configure(
            "Treeview",
            background=c_.WHITE_SMOKE['hex'],
            foreground="#000",
            rowheight=25,
            fieldbackground=c_.WHITE_SMOKE['hex'],
        )
        self.style.map(
            "Treeview",
            background=[("selected", c_.FIRE_BRICK_65['hex'])]
        )
        self.style.map(
            "TEntry",
            highlightcolor=[("focus", "#CCE6FF"), ("!focus", "")],
        )

    def create_frames(self):
        """create_frames >> Create GUI Frames

        [extended_summary]
        """
        # INSTANTIATE FRAMES
        # self.frame_header = ttk.Frame(master=self.master)
        # self.frame_top = ttk.Frame(master=self.master)
        # self.frame_bottom = ttk.Frame(master=self.master)
        FRAMES = {}
        self.frame_header = tk.Frame(
            master=self.master,
            padx=f_.padx['frame'],
            pady=f_.pady['frame'],
            background=c_.MAIN_['hex']
        )
        self.frame_top = tk.Frame(
            master=self.master,
            background=c_.MAIN_['hex']
        )
        self.frame_bottom = tk.Frame(
            master=self.master,
            padx=f_.padx['frame'],
            pady=f_.pady['frame'],
            background=c_.MAIN_['hex']
        )

        FRAMES = {
            self.frame_header: {"side": tk.TOP},
            self.frame_top: {"side": tk.TOP},
            self.frame_bottom: {"side": tk.BOTTOM}
        }

        # RENDER/PACK FRAMES
        self.frame_header.pack(
            fill=tk.BOTH,
            expand=tk.YES
        )
        self.frame_top.pack(
            fill=tk.BOTH,
            expand=tk.YES,
            side=tk.TOP,
            padx=f_.padx['pack'],
            pady=f_.pady['pack']
        )
        self.frame_bottom.pack(
            fill=tk.BOTH,
            expand=tk.YES,
            side=tk.BOTTOM,
            padx=f_.padx['pack'],
            pady=f_.pady['pack']
        )

    def create_menubar(self):
        """create_menubar [summary]

        [extended_summary]
        """
        self.menubar = tk.Menu(master=self.master)
        self.master.config(menu=self.menubar)
        self.file_ = tk.Menu(self.menubar)
        self.admin_ = tk.Menu(self.menubar)
        self.admin_database = tk.Menu(self.admin_)
        self.admin_import = tk.Menu(self.admin_)
        self.admin_export = tk.Menu(self.admin_)
        self.help_ = tk.Menu(self.menubar)
        # CASCADE
        self.menubar.add_cascade(
            menu=self.file_,
            label="File",
        )
        self.menubar.add_cascade(
            menu=self.admin_,
            label="ADMIN",
        )
        self.menubar.add_cascade(
            menu=self.help_,
            label="Help",
        )
        self.admin_.add_cascade(
            menu=self.admin_database,
            label="Database",
        )
        self.admin_.add_cascade(
            menu=self.admin_import,
            label="Import",
        )
        self.admin_.add_cascade(
            menu=self.admin_export,
            label="Export",
        )
        # COMMANDS FILE
        self.file_.add_command(
            label="Open...",
            command=lambda: print("[CLICKED] Menubar -> Open... ")
        )
        self.file_.add_separator()
        self.file_.add_command(
            label="Exit",
            command=lambda: self.master.destroy()
            # command = lambda: self.master.quit()
        )
        # COMMANDS ADMIN
        self.admin_database.add_command(
            label="New...",
            command=lambda: print("[CLICKED] Menubar -> New... ")
        )
        self.admin_database.add_command(
            label="Update...",
            command=lambda: print("[CLICKED] Menubar -> Update... ")
        )
        self.admin_database.add_command(
            label="Drop...",
            command=lambda: print("[CLICKED] Menubar -> Drop... ")
        )
        self.admin_database.add_command(
            label="Backup...",
            command=lambda: print("[CLICKED] Menubar -> Backup... ")
        )
        self.admin_database.add_command(
            label="Restore...",
            command=lambda: print("[CLICKED] Menubar -> Restore... ")
        )
        self.admin_import.add_command(
            label="Import CSV...",
            command=lambda: print("[CLICKED] Menubar -> Import CSV... ")
        )
        self.admin_import.add_command(
            label="Import JSON...",
            command=lambda: print("[CLICKED] Menubar -> Import JSON... ")
        )
        self.admin_export.add_command(
            label="Export CSV...",
            # command = db.dump_db(tn_.ACTIVE_TABLE, 'csv')
            command=lambda: print("[CLICKED] Menubar -> Export CSV... ")
            # dump_db(self, table_name, output_type)
        )
        self.admin_export.add_command(
            label="Export JSON...",
            # command = db.dump_db(tn_.ACTIVE_TABLE, 'json')
            command=lambda: print("[CLICKED] Menubar -> Export JSON... ")
        )
        # COMMANDS HELP
        self.help_.add_command(
            label="View Help",
            command=lambda: print("[CLICKED] Menubar -> View Help ")
        )
        self.help_.add_separator()
        self.help_.add_command(
            label="About...",
            command=lambda: print("[CLICKED] Menubar -> About... ")
        )
        # HOT KEYS
        self.file_.entryconfig('Open...', accelerator='Ctrl+O')
        self.file_.entryconfig('Exit', accelerator='Ctrl+E')

    def create_labels_entries_combo(self):
        """create_labels_entries_combo >> Create GUI Labels, Text Entry, and Combobox Widgets

        [extended_summary]
        """
        _MASTER = self.frame_bottom

        # HEADER WIDGET
        self.header_label = ttk.Label(
            master=self.frame_header,
            text="CAFE POS DATABASE",
            font=("bold", 36),
            anchor='center',
        )
        self.header_label.pack(
            fill=tk.BOTH,
            expand=tk.YES,
            side=tk.TOP,
        )

        # ID WIDGET
        self.id_text = tk.StringVar()
        self.id_label = ttk.Label(
            master=_MASTER,
            text=lf_.TXT[0].upper(),
            padding=lf_.padding,
            font=lf_.font,
        )
        self.id_label.grid(
            row=0,
            cnf=lf_.cnf_grid,
        )
        self.id_entry = ttk.Entry(
            master=_MASTER,
            textvariable=self.id_text,
            width=e_.width,
        )
        self.id_entry.grid(
            row=0,
            cnf=e_.cnf_grid,
        )

        # CATEGORY WIDGET
        self.category_text = tk.StringVar()
        self.category_label = ttk.Label(
            master=_MASTER,
            text=lf_.TXT[1].upper(),
            padding=lf_.padding,
            font=lf_.font,
        )
        self.category_label.grid(
            row=1,
            cnf=lf_.cnf_grid,
        )
        self.category_combo = ttk.Combobox(
            master=_MASTER,
            textvariable=self.category_text,
            values=cb_.values,
            width=cb_.width,
        )
        self.category_combo.grid(
            row=1,
            cnf=e_.cnf_grid,
        )

        # NAME WIDGET
        self.name_text = tk.StringVar()
        self.name_label = ttk.Label(
            master=_MASTER,
            text=lf_.TXT[2].upper(),
            padding=lf_.padding,
            font=lf_.font,
        )
        self.name_label.grid(
            row=2,
            cnf=lf_.cnf_grid,
        )
        self.name_entry = ttk.Entry(
            master=_MASTER,
            textvariable=self.name_text,
            width=e_.width,
        )
        self.name_entry.grid(
            row=2,
            cnf=e_.cnf_grid,
        )

        # POS LABEL WIDGET
        self.pos_label_text = tk.StringVar()
        self.pos_label_label = ttk.Label(
            master=_MASTER,
            text=lf_.TXT[3].upper(),
            padding=lf_.padding,
            font=lf_.font,
        )
        self.pos_label_label.grid(
            row=3,
            cnf=lf_.cnf_grid,
        )
        self.pos_label_entry = ttk.Entry(
            master=_MASTER,
            textvariable=self.pos_label_text,
            width=e_.width,
        )
        self.pos_label_entry.grid(
            row=3,
            cnf=e_.cnf_grid,
        )

        # PRICE WIDGET
        self.price_text = tk.StringVar()
        self.price_label = ttk.Label(
            master=_MASTER,
            text=lf_.TXT[4].upper(),
            padding=lf_.padding,
            font=lf_.font,
        )
        self.price_label.grid(
            row=4,
            cnf=lf_.cnf_grid,
        )
        self.price_entry = ttk.Entry(
            master=_MASTER,
            textvariable=self.price_text,
            width=e_.width,
        )
        self.price_entry.grid(
            row=4,
            cnf=e_.cnf_grid,
        )

    def create_treeview(self):
        """create_treeview >> Create TreeView GUI widget

        [extended_summary]
        """
        self.tree_view = ttk.Treeview(
            master=self.frame_top,
            show=tv_.show,
            selectmode=tv_.selectmode['many'],
        )

        self.vsb = ttk.Scrollbar(
            orient=tk.VERTICAL,
            command=self.tree_view.yview,
        )
        self.hsb = ttk.Scrollbar(
            orient=tk.HORIZONTAL,
            command=self.tree_view.xview,
        )

        self.tree_view['columns'] = tv_.columns['int']

        self.tree_view.heading(
            column=1,
            text=tv_.HEADINGS[0],
            # width = tkFont.Font().measure(col.title()),
            command=lambda col=1: self.sortby(self.tree_view, col, 0),
        )
        self.tree_view.heading(
            column=2,
            text=tv_.HEADINGS[1],
            # width = tkFont.Font().measure(col.title()),
            command=lambda col=2: self.sortby(self.tree_view, col, 0),
        )
        self.tree_view.heading(
            column=3,
            text=tv_.HEADINGS[2],
            # width = tkFont.Font().measure(col.title()),
            command=lambda col=3: self.sortby(self.tree_view, col, 0),
        )
        self.tree_view.heading(
            column=4,
            text=tv_.HEADINGS[3],
            # width = tkFont.Font().measure(col.title()),
            command=lambda col=4: self.sortby(self.tree_view, col, 0),
        )
        self.tree_view.heading(
            column=5,
            text=tv_.HEADINGS[4],
            # width = tkFont.Font().measure(col.title()),
            command=lambda col=5: self.sortby(self.tree_view, col, 0),
        )

        self.tree_view.column(
            column=1,
            anchor=tk.W,
            width=75,
            minwidth=50,
            # stretch = tk.YES,
        )
        self.tree_view.column(
            column=2,
            anchor=tk.W,
            width=100,
            minwidth=80,
            # stretch = tk.YES,
        )
        self.tree_view.column(
            column=3,
            anchor=tk.W,
            width=155,
            minwidth=125,
            # stretch = tk.YES,
        )
        self.tree_view.column(
            column=4,
            anchor=tk.W,
            width=125,
            minwidth=100
            # stretch = tk.YES
        )
        self.tree_view.column(
            column=5,
            anchor=tk.CENTER,
            width=60,
            minwidth=40,
            # stretch = tk.YES,
        )

        self.tree_view.configure(
            yscrollcommand=self.vsb.set,
            xscrollcommand=self.hsb.set,
        )
        self.tree_view.tag_configure(
            tagname='row_odd',
            background=c_.WHITE_SMOKE['hex'],
        )
        self.tree_view.tag_configure(
            tagname='row_even',
            background=c_.GAINSBORO['hex'],
        )

        self.tree_view.grid(
            column=0,
            row=0,
            sticky='nsew',
            in_=self.frame_top,
        )
        self.vsb.grid(
            column=1,
            row=0,
            sticky='ns',
            in_=self.frame_top,
        )
        self.hsb.grid(
            column=0,
            row=1,
            sticky='ew',
            in_=self.frame_top,
        )

        self.frame_top.grid_columnconfigure(
            index=0,
            weight=1,
        )
        self.frame_top.grid_rowconfigure(
            index=0,
            weight=1,
        )

        self.tree_view.bind(
            sequence=tv_.bind_seq,
            func=self.select_item,
        )

        # TODO: COMPLETE IMPLEMENTATION
        '''
        adjust_column_width():
                for item in items:
                    self.tree_view.insert('', 'end', values = item)
                    # adjust column width as necessary to fit data
                    for i, val in enumerate(item):
                        col_w = tkFont.Font().measure(val)
                        if self.tree_view.column(items_header[i],width = None)<col_w:
                            self.tree_view.column(items_header[i], width = col_w)
        '''

        # TEST DATA
        # test_data = [
        #     ("ID001", "Category01", "ItemName01", "Label01", 1.95),
        #     ("ID002", "Category02", "ItemName02", "Label02", 2.95),
        #     ("ID003", "Category03", "ItemName03", "Label03", 3.95),
        #     ("ID004", "Category04", "ItemName04", "Label04", 4.95),
        #     ("ID005", "Category05", "ItemName05", "Label05", 5.95)
        # ]
        # for i, item in enumerate(test_data):
        #     self.tree_view.insert(parent = "", index = tk.END, iid = i, text = "", values = item)

    def create_buttons(self):
        """create_buttons >> Add button widgets to frame(s) -> ADD, REMOVE, UPDATE, CLEAR, SEARCH, ...

        [extended_summary]
        """
        _MASTER = self.frame_bottom

        # BUTTON 01
        self.add_btn = ttk.Button(
            master=_MASTER,
            text=b_.BTN['01']['text'].upper(),
            command=self.add_item,
            # cnf = b_.cnf,
        )
        self.add_btn.grid(
            row=b_.BTN['01']['row'],
            column=b_.BTN['01']['column'],
            cnf=b_.cnf_grid,
        )

        # BUTTON 02
        self.remove_btn = ttk.Button(
            master=_MASTER,
            text=b_.BTN['02']['text'].upper(),
            command=self.remove_item,
            # cnf = b_.cnf,
        )
        self.remove_btn.grid(
            row=b_.BTN['02']['row'],
            column=b_.BTN['02']['column'],
            cnf=b_.cnf_grid,
        )

        # BUTTON 03
        self.update_btn = ttk.Button(
            master=_MASTER,
            text=b_.BTN['03']['text'].upper(),
            command=self.update_item,
            # cnf = b_.cnf,
        )
        self.update_btn.grid(
            row=b_.BTN['03']['row'],
            column=b_.BTN['03']['column'],
            cnf=b_.cnf_grid,
        )

        # BUTTON 04
        self.clear_btn = ttk.Button(
            master=_MASTER,
            text=b_.BTN['04']['text'].upper(),
            command=self.clear_entry_fields,
            # cnf = b_.cnf,
        )
        self.clear_btn.grid(
            row=b_.BTN['04']['row'],
            column=b_.BTN['04']['column'],
            cnf=b_.cnf_grid,
        )

        # BUTTON 05
        # self.import_csv_btn = ttk.Button(
        #     master = _MASTER, 
        #     text = b_.BTN['05']['text'].upper(), 
        #     command = lambda: print(f"{b_.BTN['05']['text'].upper()} Clicked!"), 
        #     # cnf = b_.cnf,
        # )
        # self.import_csv_btn.grid(
        #     row = b_.BTN['05']['row'], 
        #     column = b_.BTN['05']['column'], 
        #     cnf = b_.cnf_grid,
        # )

        # BUTTON 06
        # self.export_csv_btn = ttk.Button(
        #     master = _MASTER, 
        #     text = b_.BTN['06']['text'].upper(), 
        #     command = lambda: print(f"{b_.BTN['06']['text'].upper()} Clicked!"), 
        #     # cnf = b_.cnf,
        # )
        # self.export_csv_btn.grid(
        #     row = b_.BTN['06']['row'], 
        #     column = b_.BTN['06']['column'], 
        #     cnf = b_.cnf_grid,
        # )

        # # BUTTON 07
        # self.search_menubtn = ttk.Menubutton(
        #     master = _MASTER, 
        #     text = b_.BTN['07']['text'].upper(),
        #     direction='above'
        #     # command = lambda: print(f"{b_.BTN['07']['text'].upper()} Clicked!"), 
        #     # cnf = b_.cnf,
        # )
        # self.search_menubtn.grid(
        #     row = b_.BTN['07']['row'], 
        #     column = b_.BTN['07']['column'], 
        #     columnspan = b_.BTN['07']['columnspan'], 
        #     cnf = b_.cnf_grid,
        # )
        # self.search_menubtn.menu = tk.Menu(self.search_menubtn)   
        # self.search_menubtn["menu"] = self.search_menubtn.menu
        # self.mb_option_id = tk.IntVar()
        # self.mb_option_category = tk.IntVar()
        # self.mb_option_name = tk.IntVar()
        # self.mb_option_label = tk.IntVar()
        # self.mb_option_price = tk.IntVar()

        # # self.search_menubtn.menu.add_checkbutton(
        # self.search_menubtn.menu.add_radiobutton(
        #     label = "Item ID",
        #     variable = self.mb_option_id
        # )
        # # self.search_menubtn.menu.add_checkbutton(
        # self.search_menubtn.menu.add_radiobutton(
        #     label = "Category",
        #     variable = self.mb_option_category
        # )
        # # self.search_menubtn.menu.add_checkbutton(
        # self.search_menubtn.menu.add_radiobutton(
        #     label = "Name",
        #     variable = self.mb_option_name
        # )
        # # self.search_menubtn.menu.add_checkbutton(
        # self.search_menubtn.menu.add_radiobutton(
        #     label = "Label",
        #     variable = self.mb_option_label
        # )
        # # self.search_menubtn.menu.add_checkbutton(
        # self.search_menubtn.menu.add_radiobutton(
        #     label = "Price",
        #     variable = self.mb_option_price
        # )

        # SEARCH COMBOBOX (BUTTON 07)
        self.search_combo = ttk.Combobox(
            master=_MASTER,
            # textvariable = None,
            values=cb_.search_values,
            width=cb_.width,
            style="Search.TCombobox",
        )
        self.search_combo.set(cb_.search_values[0])
        self.search_combo.grid(
            row=3,
            column=2,
            columnspan=2,
        )

        # BUTTON 08
        self.search_btn = ttk.Button(
            master=_MASTER,
            text=b_.BTN['08']['text'].upper(),
            command=self.search_item_id,
            # cnf = b_.cnf,
        )
        self.search_btn.grid(
            row=b_.BTN['08']['row'],
            column=b_.BTN['08']['column'],
            cnf=b_.cnf_grid,
        )

        # BUTTON 09
        self.populate_btn = ttk.Button(
            master=_MASTER,
            text=b_.BTN['09']['text'].upper(),
            command=self.populate_tree,
            # cnf = b_.cnf,
        )
        self.populate_btn.grid(
            row=b_.BTN['09']['row'],
            column=b_.BTN['09']['column'],
            cnf=b_.cnf_grid,
        )

    def populate_tree(self):
        """populate_tree >> Populate Treview with data

        [extended_summary]
        """
        self.clear_entry_fields()
        self.tree_view.delete(*self.tree_view.get_children())
        for i, row in enumerate(db.fetch_all_records()):
            if i % 2 == 0:
                self.tree_view.insert("", "end", values=row, tags=('row_even',))
            else:
                self.tree_view.insert("", "end", values=row, tags=('row_odd',))

    def validate_conditions(self, action: str):
        """validate_conditions >> Validate User Input Fields

        [extended_summary]

        :param action: [description]
        :type action: str
        :return: [description]
        :rtype: [type]
        """
        item = {
            "id_": self.id_text.get().upper(),
            "category_": self.category_text.get().lower(),
            "name_": self.name_text.get().capitalize(),
            "pos_label_": self.pos_label_text.get().upper(),
            "price_": float(self.price_text.get()) if self.price_text.get() != '' else self.price_text.get(),
        }
        conditions = [
            item['id_'] == '',
            item['category_'] == '',
            item['name_'] == '',
            item['pos_label_'] == '',
            item['price_'] == ''
        ]
        if any(conditions):
            if action == 'add':
                messagebox.showerror(
                    m_.ERRORS['add_item']['title'],
                    m_.ERRORS['add_item']['message']
                )
            elif action == 'update':
                messagebox.showerror(
                    m_.ERRORS['update_item']['title'],
                    m_.ERRORS['update_item']['message']
                )
            return True
        return False

    def add_item(self):
        """add_item >> Add item (record) into database and ListBox widget

        [extended_summary]
        """
        new_item = {
            "id_": self.id_text.get().upper(),
            "category_": self.category_text.get().lower(),
            "name_": self.name_text.get().capitalize(),
            "pos_label_": self.pos_label_text.get().upper(),
            "price_": float(self.price_text.get()) if self.price_text.get() != '' else self.price_text.get(),
        }
        if self.validate_conditions(action='add'):
            return
        # DEBUG ==========================
        print(self.id_text.get().upper())
        # ================================
        db.insert_record(
            new_item['id_'],
            new_item['category_'],
            new_item['name_'],
            new_item['pos_label_'],
            new_item['price_']
        )
        self.populate_tree()

    def select_item(self, _):
        """select_item >> Insert selected item (record) into respective text fields [_ : event]

        [extended_summary]

        :param _: [description]
        :type _: [type]
        """
        # global self.selected_item_values
        try:
            self.selected_item_values = self.tree_view.item(self.tree_view.focus(), 'values')
            # DEBUG ==========================================================
            print(f"{self.tree_view.focus()} -> {self.selected_item_values}")
            print(f"{self.tree_view.selection()} -> {self.selected_item_values}")
            # ================================================================
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(tk.END, self.selected_item_values[0])
            self.category_combo.delete(0, tk.END)
            self.category_combo.insert(tk.END, self.selected_item_values[1])
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, self.selected_item_values[2])
            self.pos_label_entry.delete(0, tk.END)
            self.pos_label_entry.insert(tk.END, self.selected_item_values[3])
            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(tk.END, self.selected_item_values[4])
        except IndexError as err:
            print(f"{err} <=> {err.text}")
        except Exception as err:
            print(f"{err} <=> {err.text}")

    # TODO: rename -> remove_item_single
    def remove_item(self):
        """remove_item >> Remove item (record)

        [extended_summary]
        """
        if messagebox.askyesno(
                title=m_.DELETE['title'],
                message=f"{m_.DELETE['message']} {self.selected_item_values[0]}"
        ):
            db.remove_record(self.selected_item_values[0])
            self.populate_tree()

    # TODO: finish implementation
    def remove_item_many(self):
        """remove_item_many >> Remove Multiple Selected Items

        [extended_summary]
        """
        records_selected = self.tree_view.selection()
        if messagebox.askyesno(
                title=m_.DELETE['title'],
                message=f"{m_.DELETE['message']} {records_selected.count()}"
        ):
            for record in records_selected:
                db.remove_record(record)
            self.populate_tree()

    def update_item(self):
        """update_item >> Update item (record)

        [extended_summary]
        """
        if self.validate_conditions(action='update'):
            return
        else:
            if messagebox.askyesno(
                    title=m_.UPDATE['title'],
                    message=f"{m_.UPDATE['message']} {self.selected_item_values[0]}"
            ):
                db.update_record(
                    self.selected_item_values[0],
                    self.category_text.get().lower(),
                    self.name_text.get().capitalize(),
                    self.pos_label_text.get().upper(),
                    float(self.price_text.get())
                )
                self.populate_tree()

    def clear_entry_fields(self):
        """clear_entry_fields >> Clear text fields

        [extended_summary]
        """
        self.id_entry.delete(0, tk.END)
        self.category_combo.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.pos_label_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def search_item(self):
        """Search Item"""
        pass

    def search_item_id(self):
        """search_item_id >> Search by item ID

        [extended_summary]
        """
        if not self.id_entry.get():
            print("ID BLANK -> ADD Prompt!")
        else:
            self.tree_view.delete(*self.tree_view.get_children())
            for row in db.search_record_id(self.id_entry.get().upper()):
                self.tree_view.insert("", "end", values=row)

    def sortby(self, tree_view: object, column: int, descending: int):
        """sortby >> Sort Treeview on click event

        [extended_summary]

        :param tree_view: [description]
        :type tree_view: object (TreeView)
        :param column: [description]
        :type column: int
        :param descending: [description]
        :type descending: int
        """
        print(f"Header Cell {column} Clicked")
        # numeric data -> change to float
        # data =  change_numeric(data)
        data = [(self.tree_view.set(child, column), child) for child in self.tree_view.get_children('')]
        data.sort(reverse=descending)
        for i, item in enumerate(data):
            self.tree_view.move(item[1], '', i)
        # switch heading -> opposite sort
        self.tree_view.heading(
            column,
            command=lambda column=column: self.sortby(tree_view, column, int(not descending))
        )


def main():
    root = tk.Tk()
    root.option_add('*tearOff', False)

    SCREEN_WIDTH = root.winfo_screenwidth()
    SCREEN_HEIGHT = root.winfo_screenheight()
    APP_WIDTH = 650
    APP_HEIGHT = 625
    X = (SCREEN_WIDTH / 2) - (APP_WIDTH / 2)
    Y = (SCREEN_HEIGHT / 2) - (APP_HEIGHT / 2)

    gui = GUI(master=root, app_width=APP_WIDTH, app_height=APP_HEIGHT, x=X, y=Y)
    gui.mainloop()


if __name__ == '__main__':
    main()
