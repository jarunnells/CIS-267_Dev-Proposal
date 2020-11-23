# ==========================================
#     DEVELOPER:  J.A. Runnells
#          FILE:  app_gui.py
#        BRANCH: dev
# ==========================================
# STANDARD LIBRARY IMPORTS
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from tkinter import messagebox
from tkinter import ttk as ttk

# CUSTOM LIBRARY IMPORTS
# from modules.DBManager import DBManager
from modules.database import Database
from modules.config import Messages as m_
from modules.config import Query as q_
from modules.config import Colors as c_
from modules.config import FrameWidget as f_
from modules.config import TreeViewWidget as tv_
from modules.config import ButtonWidget as b_
from modules.config import InputFieldWidget as if_
from modules.config import ListBox as lb_
from modules.config import BarScroll as bs_
from modules.config import LabelField as lf_
from modules.config import VarString as vs_
from modules.config import StylesTtk as st_

db = Database(":memory:")
db.insert_record("BK001", "bkfast", "Muffin 01", "MUFFIN 01", 2.75)
db.insert_record("BK002", "bkfast", "Muffin 02", "MUFFIN 02", 2.75)
db.insert_record("BK003", "bkfast", "Muffin 03", "MUFFIN 03", 2.75)
db.insert_record("HB001", "bev_hot", "Coffee 01", "COFFEE 01", 1.99)
db.insert_record("HB002", "bev_hot", "Coffee 02", "COFFEE 02", 1.99)
db.insert_record("HB003", "bev_hot", "Coffee 03", "COFFEE 03", 1.99)
db.insert_record("CB001", "bev_cold", "Aquafina 01", "AQUA H20 01", 1.09)
db.insert_record("CB002", "bev_cold", "Aquafina 02", "AQUA H20 02", 1.25)
db.insert_record("CB003", "bev_cold", "Aquafina 03", "AQUA H20 03", 1.05)
db.insert_record("DE001", "deli", "Noodle Cup 01", "NOODLE CUP 01", 1.25)
db.insert_record("DE002", "deli", "Noodle Cup 02", "NOODLE CUP 02", 1.29)
db.insert_record("DE003", "deli", "Noodle Cup 03", "NOODLE CUP 03", 1.82)
db.insert_record("SN001", "snack", "House Cookie 01", "HOUSE COOKIE 01", 1.64)
db.insert_record("SN002", "snack", "House Cookie 02", "HOUSE COOKIE 02", 1.64)
db.insert_record("SN003", "snack", "House Cookie 03", "HOUSE COOKIE 03", 1.64)
db.insert_record("CD001", "condiment", "Dressing 01", "DRESSING 01", 0.75)
db.insert_record("CD002", "condiment", "Dressing 02", "DRESSING 02", 0.75)
db.insert_record("CD003", "condiment", "Dressing 03", "DRESSING 03", 0.75)

# TXT = [
#     ["Item ID", "Category", "Name", "POS Label", "Price"],
#     ["Add Item", "Remove Item", "Update Item", "Clear Input"]
# ]
# ERRORS = {
#     "title": "REQUIRED!",
#     "message": "ALL fields required."
# }
# COLORS = {
#     "light_steel_blue": {"py_name": "light steel blue", "hex": "#B0C4DE", "rgb": (176, 196, 222)},
#     "light_coral": {"py_name": "light coral", "hex": "#F08080", "rgb": (240, 128, 128)},
#     "lavender": {"py_name": "lavender", "hex": "#E6E6FA", "rgb": (230, 230, 250)},
#     "antique_white": {"py_name": "antique white", "hex": "#FAEBD7", "rgb": (250, 235, 215)},
# }


# TODO: FINISH IMPLEMENTATION -> config.py
class GUI(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master        
        master.title("Cafe POS Database Management")
        master.geometry("650x600")
        # master['bg'] = COLORS['light_steel_blue']['py_name']
        master['bg'] = c_.DARK_SEA_GREEN['hex']
        self.initialize_UI()
    
    def initialize_UI(self):
        self.selected_item_values = 0
        self.create_frames()
        self.create_labels_entries()
        self.create_buttons()
        # self.create_listbox()
        self.create_treeview()
        self.create_styles()
        # self.populate_list()
        self.populate_tree()

    def create_styles(self):
        self.style = ttk.Style()
        self.style.theme_use(st_.THEMES[2])
        self.style.configure(
            "Treeview",
            background=c_.WHITE_SMOKE['hex'],
            foreground="#000",
            rowheight=25,
            fieldbackground=c_.WHITE_SMOKE['hex']
        )
        self.style.map("Treeview", background=[("selected", c_.FIRE_BRICK_65['hex'])])

    def create_frames(self):
        """Create GUI Frames"""
        # INSTANTIATE FRAMES
        self.frame_header = tk.Frame(master=self.master, padx=f_.padx['frame'], pady=f_.pady['frame'], background=c_.DARK_SEA_GREEN['hex'])
        self.frame_top = tk.Frame(master=self.master, background=c_.DARK_SEA_GREEN['hex'])
        self.frame_bottom = tk.Frame(master=self.master, padx=f_.padx['frame'], pady=f_.pady['frame'], background=c_.DARK_SEA_GREEN['hex'])

        # RENDER/PACK FRAMES
        self.frame_header.pack(fill=tk.BOTH, expand=tk.YES)
        self.frame_top.pack(fill=tk.BOTH, expand=tk.YES, side=tk.TOP, padx=f_.padx['pack'], pady=f_.pady['pack'])
        self.frame_bottom.pack(fill=tk.BOTH, expand=tk.YES, side=tk.BOTTOM, padx=f_.padx['pack'], pady=f_.pady['pack'])

    def create_labels_entries(self):
        """Create GUI Labels and Text Entry Fields"""
        _MASTER = self.frame_bottom

        # HEADER WIDGET
        self.header_label = tk.Label(
            master=self.frame_header, text="CAFE POS DATABASE", font=("bold", 36), padx=0, pady=0, background=c_.DARK_SEA_GREEN['hex'], foreground="#8B0000")
        self.header_label.pack(fill=tk.BOTH, expand=tk.YES, side=tk.TOP)

        # ID WIDGET
        self.id_text = tk.StringVar()
        self.id_label = tk.Label(
            master=_MASTER, text=lf_.TXT[0].upper(), cnf=lf_.cnf)
        self.id_label.grid(row=0, cnf=lf_.cnf_grid)
        self.id_entry = tk.Entry(master=_MASTER, textvariable=self.id_text)
        self.id_entry.grid(row=0, cnf=if_.cnf_grid)

        # CATEGORY WIDGET
        self.category_text = tk.StringVar()
        self.category_label = tk.Label(
            master=_MASTER, text=lf_.TXT[1].upper(), cnf=lf_.cnf)
        self.category_label.grid(row=1, cnf=lf_.cnf_grid)
        self.category_entry = tk.Entry(
            master=_MASTER, textvariable=self.category_text)
        self.category_entry.grid(row=1, cnf=if_.cnf_grid)

        # NAME WIDGET
        self.name_text = tk.StringVar()
        self.name_label = tk.Label(
            master=_MASTER, text=lf_.TXT[2].upper(), cnf=lf_.cnf)
        self.name_label.grid(row=2, cnf=lf_.cnf_grid)
        self.name_entry = tk.Entry(
            master=_MASTER, textvariable=self.name_text)
        self.name_entry.grid(row=2, cnf=if_.cnf_grid)

        # POS LABEL WIDGET
        self.pos_label_text = tk.StringVar()
        self.pos_label_label = tk.Label(
            master=_MASTER, text=lf_.TXT[3].upper(), cnf=lf_.cnf)
        self.pos_label_label.grid(row=3, cnf=lf_.cnf_grid)
        self.pos_label_entry = tk.Entry(
            master=_MASTER, textvariable=self.pos_label_text)
        self.pos_label_entry.grid(row=3, cnf=if_.cnf_grid)

        # PRICE WIDGET
        self.price_text = tk.StringVar()
        self.price_label = tk.Label(
            master=_MASTER, text=lf_.TXT[4].upper(), cnf=lf_.cnf)
        self.price_label.grid(row=4, cnf=lf_.cnf_grid)
        self.price_entry = tk.Entry(master=_MASTER, textvariable=self.price_text)
        self.price_entry.grid(row=4, cnf=if_.cnf_grid)

        # SEARCH WIDGET
        # self.search_text = tk.StringVar()
        # self.search_label = tk.Label(
        #     master=_MASTER, text=lf_.TXT[5].upper(), cnf=lf_.cnf)
        # self.search_label.grid(row=5, cnf=lf_.cnf_grid)
        # self.search_entry = tk.Entry(master=_MASTER, textvariable=self.search_text)
        # self.search_entry.grid(row=5, cnf=if_.cnf_grid)

    def create_treeview(self):
        """Create TreeView GUI widget"""
        self.tree_view = ttk.Treeview(
            master=self.frame_top, show=tv_.show, selectmode=tv_.selectmode['many'])

        self.vsb = ttk.Scrollbar(orient="vertical", command=self.tree_view.yview)
        self.hsb = ttk.Scrollbar(orient="horizontal", command=self.tree_view.xview)

        self.tree_view['columns'] = tv_.columns['int']

        self.tree_view.heading(1, text=tv_.HEADINGS[0], command=lambda col=1: self.sortby(self.tree_view, col, 0))  # width=tkFont.Font().measure(col.title())
        self.tree_view.heading(2, text=tv_.HEADINGS[1], command=lambda col=2: self.sortby(self.tree_view, col, 0))  # width=tkFont.Font().measure(col.title())
        self.tree_view.heading(3, text=tv_.HEADINGS[2], command=lambda col=3: self.sortby(self.tree_view, col, 0))  # width=tkFont.Font().measure(col.title())
        self.tree_view.heading(4, text=tv_.HEADINGS[3], command=lambda col=4: self.sortby(self.tree_view, col, 0))  # width=tkFont.Font().measure(col.title())
        self.tree_view.heading(5, text=tv_.HEADINGS[4], command=lambda col=5: self.sortby(self.tree_view, col, 0))  # width=tkFont.Font().measure(col.title())

        self.tree_view.column(1, anchor=tk.W, width=75, minwidth=50)  # stretch=tk.YES
        self.tree_view.column(2, anchor=tk.W, width=100, minwidth=80)  # stretch=tk.YES
        self.tree_view.column(3, anchor=tk.W, width=155, minwidth=125)  # stretch=tk.YES
        self.tree_view.column(4, anchor=tk.W, width=125, minwidth=100)  # stretch=tk.YES
        self.tree_view.column(5, anchor=tk.CENTER, width=60, minwidth=40)  # stretch=tk.YES

        self.tree_view.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        self.tree_view.tag_configure('row_odd', background=c_.WHITE_SMOKE['hex'])
        self.tree_view.tag_configure('row_even', background=c_.GAINSBORO['hex'])
        
        self.tree_view.grid(column=0, row=0, sticky='nsew', in_=self.frame_top)
        self.vsb.grid(column=1, row=0, sticky='ns', in_=self.frame_top)
        self.hsb.grid(column=0, row=1, sticky='ew', in_=self.frame_top)

        self.frame_top.grid_columnconfigure(0, weight=1)
        self.frame_top.grid_rowconfigure(0, weight=1)

        self.tree_view.bind(tv_.bind_seq, self.select_item)
        
        # TODO: COMPLETE IMPLEMENTATION
        '''
        adjust_column_width():
                for item in items:
                    self.tree_view.insert('', 'end', values=item)
                    # adjust column width as necessary to fit data
                    for i, val in enumerate(item):
                        col_w = tkFont.Font().measure(val)
                        if self.tree_view.column(items_header[i],width=None)<col_w:
                            self.tree_view.column(items_header[i], width=col_w)
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
        #     self.tree_view.insert(parent="", index=tk.END, iid=i, text="", values=item)

    def create_listbox(self):
        """Create ListBox GUI widget"""
        _MASTER = self.frame_bottom

        # ITEMS LIST -> listbox
        self.items_list = tk.Listbox(master=_MASTER, cnf=lb_.cnf)
        self.items_list.grid(cnf=lb_.cnf_grid)

        # SCROLLBAR WIDGET
        self.scrollbar = tk.Scrollbar(master=_MASTER)
        self.scrollbar.grid(cnf=bs_.cnf_grid)

        # SET SCROLLBAR WIDGET
        self.items_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.items_list.yview)

        # BIND LISTBOX SELECTION
        self.items_list.bind(lb_.bind_seq, self.select_item)

    def create_buttons(self):
        """Add button widgets to frame(s) -> ADD, REMOVE, UPDATE, CLEAR, SEARCH, ..."""
        _MASTER = self.frame_bottom

        # BUTTON 01
        self.add_btn = tk.Button(
            master=_MASTER, text=b_.BTN['01']['text'].upper(), command=self.add_item, cnf=b_.cnf)
        self.add_btn.grid(row=b_.BTN['01']['row'], column=b_.BTN['01']['column'], cnf=b_.cnf_grid)
        
        # BUTTON 02
        self.remove_btn = tk.Button(
            master=_MASTER, text=b_.BTN['02']['text'].upper(), command=self.remove_item, cnf=b_.cnf)
        self.remove_btn.grid(row=b_.BTN['02']['row'], column=b_.BTN['02']['column'], cnf=b_.cnf_grid)
        
        # BUTTON 03
        self.update_btn = tk.Button(
            master=_MASTER, text=b_.BTN['03']['text'].upper(), command=self.update_item, cnf=b_.cnf)
        self.update_btn.grid(row=b_.BTN['03']['row'], column=b_.BTN['03']['column'], cnf=b_.cnf_grid)
        
        # BUTTON 04
        self.clear_btn = tk.Button(
            master=_MASTER, text=b_.BTN['04']['text'].upper(), command=self.clear_text, cnf=b_.cnf)
        self.clear_btn.grid(row=b_.BTN['04']['row'], column=b_.BTN['04']['column'], cnf=b_.cnf_grid)
        
        # BUTTON 05
        self.import_csv_btn = tk.Button(
            master=_MASTER, text=b_.BTN['05']['text'].upper(), command=lambda: print(f"{b_.BTN['05']['text'].upper()} Clicked!"), cnf=b_.cnf)
        self.import_csv_btn.grid(row=b_.BTN['05']['row'], column=b_.BTN['05']['column'], cnf=b_.cnf_grid)
        
        # BUTTON 06
        self.export_csv_btn = tk.Button(
            master=_MASTER, text=b_.BTN['06']['text'].upper(), command=lambda: print(f"{b_.BTN['06']['text'].upper()} Clicked!"), cnf=b_.cnf)
        self.export_csv_btn.grid(row=b_.BTN['06']['row'], column=b_.BTN['06']['column'], cnf=b_.cnf_grid)
        
        # BUTTON 07
        self.import_json_btn = tk.Button(
            master=_MASTER, text=b_.BTN['07']['text'].upper(), command=lambda: print(f"{b_.BTN['07']['text'].upper()} Clicked!"), cnf=b_.cnf)
        self.import_json_btn.grid(row=b_.BTN['07']['row'], column=b_.BTN['07']['column'], columnspan=b_.BTN['07']['columnspan'], cnf=b_.cnf_grid)
        
        # BUTTON 08
        self.search_btn = tk.Button(
            master=_MASTER, text=b_.BTN['08']['text'].upper(), command=self.search_item_id, cnf=b_.cnf)
        self.search_btn.grid(row=b_.BTN['08']['row'], column=b_.BTN['08']['column'], cnf=b_.cnf_grid)
        
        # BUTTON 09
        self.populate_btn = tk.Button(
            master=_MASTER, text=b_.BTN['09']['text'].upper(), command=self.populate_tree, cnf=b_.cnf)
        self.populate_btn.grid(row=b_.BTN['09']['row'], column=b_.BTN['09']['column'], cnf=b_.cnf_grid)

    def populate_tree(self):
        self.clear_text()
        self.tree_view.delete(*self.tree_view.get_children())
        for i, row in enumerate(db.fetch_all_records()):
            if i % 2 == 0:
                self.tree_view.insert("", "end", values=row, tags=('row_even',))
            else:
                self.tree_view.insert("", "end", values=row, tags=('row_odd',))

    def validate_conditions(self):
        item = {
            "id_": self.id_text.get().upper(),
            "category_": self.category_text.get().lower(),
            "name_": self.name_text.get().capitalize(),
            "pos_label_": self.pos_label_text.get().upper(),
            "price_": float(self.price_text.get()),
        } 
        conditions = [
            item['id_'] == '',
            item['category_'] == '',
            item['name_'] == '',
            item['pos_label_'] == '',
            item['price_'] == ''
        ]
        return conditions

    def add_item(self):
        """Add item (record) into database and ListBox widget"""
        new_item = {
            "id_": self.id_text.get().upper(),
            "category_": self.category_text.get().lower(),
            "name_": self.name_text.get().capitalize(),
            "pos_label_": self.pos_label_text.get().upper(),
            "price_": float(self.price_text.get()),
        }        
        # conditions = [
        #     new_item['id_'] == '',
        #     new_item['category_'] == '',
        #     new_item['name_'] == '',
        #     new_item['pos_label_'] == '',
        #     new_item['price_'] == ''
        # ]
        if any(self.validate_conditions()):
            messagebox.showerror(m_.ERRORS['add_item']['title'], m_.ERRORS['add_item']['message'])
            return
        # DEBUG ==========================
        print(self.id_text.get().upper())
        # ================================
        db.insert_record(
            new_item['id_'], new_item['category_'], new_item['name_'], new_item['pos_label_'], new_item['price_'])
        self.populate_tree()

    def select_item(self, _):
        """Insert selected item (record) into respective text fields

        Args:
            event ([type]): [description]
        """
        # global self.selected_item_values
        try:
            self.selected_item_values = self.tree_view.item(self.tree_view.focus(), 'values')
            # DEBUG ==========================================================
            print(f"{self.tree_view.focus()} -> {self.selected_item_values}")
            # ================================================================
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(tk.END, self.selected_item_values[0])
            self.category_entry.delete(0, tk.END)
            self.category_entry.insert(tk.END, self.selected_item_values[1])
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
        """Remove item (record)"""
        if messagebox.askyesno(title=m_.DELETE['title'], message=f"{m_.DELETE['message']} {self.selected_item_values[0]}"):
            db.remove_record(self.selected_item_values[0])
            self.populate_tree()

    # TODO: finish implementation
    def remove_item_many(self):
        """Remove Multiple Selected Items"""
        records_selected = self.tree_view.selection()
        if messagebox.askyesno(title=m_.DELETE['title'], message=f"{m_.DELETE['message']} {records_selected.count()}"):
            for record in records_selected:
                db.remove_record(record)
            self.populate_tree()

    def update_item(self):
        """Update item (record)"""
        # updated_item = {
        #     "id_": self.id_text.get().upper(),
        #     "category_": self.category_text.get().lower(),
        #     "name_": self.name_text.get().capitalize(),
        #     "pos_label_": self.pos_label_text.get().upper(),
        #     "price_": float(self.price_text.get()),
        # } 
        # conditions = [
        #     updated_item['id_'] == '',
        #     updated_item['category_'] == '',
        #     updated_item['name_'] == '',
        #     updated_item['pos_label_'] == '',
        #     updated_item['price_'] == ''
        # ]
        if any(self.validate_conditions()):
            messagebox.showerror(m_.ERRORS['update_item']['title'], m_.ERRORS['update_item']['message'])
        else:
            if messagebox.askyesno(title=m_.UPDATE['title'], message=f"{m_.UPDATE['message']} {self.selected_item_values[0]}"):
                db.update_record(
                    self.selected_item_values[0],
                    self.category_text.get().lower(),
                    self.name_text.get().capitalize(),
                    self.pos_label_text.get().upper(),
                    float(self.price_text.get())
                )
                self.populate_tree()

    def clear_text(self):
        """Clear text fields"""
        self.id_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.pos_label_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        # self.search_entry.delete(0, tk.END)

    def search_item_id(self):
        """Search by item ID"""
        if not self.id_entry.get():
            print("ID BLANK -> ADD Prompt!")
        else:
            self.tree_view.delete(*self.tree_view.get_children())
            for row in db.search_record_id(self.id_entry.get().upper()):
                self.tree_view.insert("", "end", values=row)

    def sortby(self, tree_view, column, descending):
        """Sort Treeview on click event"""
        print(f"Header Cell {column} Clicked")
        # numeric data -> change to float
        # data =  change_numeric(data)
        data = [(self.tree_view.set(child, column), child) for child in self.tree_view.get_children('')]
        data.sort(reverse=descending)
        for ix, item in enumerate(data):
            self.tree_view.move(item[1], '', ix)
        # switch heading -> opposite sort
        self.tree_view.heading(column, command=lambda c=column: self.sortby(tree_view, c, int(not descending)))

def main():
    root = tk.Tk()
    root.minsize(width=600, height=550)
    gui = GUI(master=root)
    gui.mainloop()


if __name__ == '__main__':
    main()
