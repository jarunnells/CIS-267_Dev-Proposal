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
from data.database import Database
from modules.config import Messages as m_
from modules.config import Query as q_
from modules.config import Colors as c_
from modules.config import TreeViewWidget as tv_
from modules.config import ButtonWidget as b_
from modules.config import InputFieldWidget as if_
from modules.config import ListBox as lb_
from modules.config import BarScroll as bs_
from modules.config import LabelField as lf_
from modules.config import VarString as vs_
from modules.config import MessageBoxWidget as mb_

db = Database(":memory:")
db.insert("BK001", "bkfast", "Muffin", "MUFFIN", 2.75)
db.insert("HB001", "bev_hot", "Coffee", "COFFEE", 1.99)
db.insert("CB001", "bev_cold", "Aquafina", "AQUA H20", 1.00)
db.insert("DE001", "deli", "Noodle Cup", "NOODLE CUP", 1.00)
db.insert("SN001", "snack", "House Cookie", "HOUSE COOKIE", 1.64)
db.insert("CD001", "condiment", "Dressing", "DRESSING", 0.75)
db.insert("BK002", "bkfast", "Muffin", "MUFFIN", 2.75)
db.insert("HB002", "bev_hot", "Coffee", "COFFEE", 1.99)
db.insert("CB002", "bev_cold", "Aquafina", "AQUA H20", 1.00)
db.insert("DE002", "deli", "Noodle Cup", "NOODLE CUP", 1.00)
db.insert("SN002", "snack", "House Cookie", "HOUSE COOKIE", 1.64)
db.insert("CD002", "condiment", "Dressing", "DRESSING", 0.75)
db.insert("BK003", "bkfast", "Muffin", "MUFFIN", 2.75)
db.insert("HB003", "bev_hot", "Coffee", "COFFEE", 1.99)
db.insert("CB003", "bev_cold", "Aquafina", "AQUA H20", 1.00)
db.insert("DE003", "deli", "Noodle Cup", "NOODLE CUP", 1.00)
db.insert("SN003", "snack", "House Cookie", "HOUSE COOKIE", 1.64)
db.insert("CD003", "condiment", "Dressing", "DRESSING", 0.75)

TXT = [
    ["Item ID", "Category", "Name", "POS Label", "Price"],
    ["Add Item", "Remove Item", "Update Item", "Clear Input"]
]
ERRORS = {
    "title": "REQUIRED!",
    "message": "ALL fields required."
}
COLORS = {
    "light_steel_blue": {"py_name": "light steel blue", "hex": "#B0C4DE", "rgb": (176, 196, 222)},
    "light_coral": {"py_name": "light coral", "hex": "#F08080", "rgb": (240, 128, 128)},
    "lavender": {"py_name": "lavender", "hex": "#E6E6FA", "rgb": (230, 230, 250)},
    "antique_white": {"py_name": "antique white", "hex": "#FAEBD7", "rgb": (250, 235, 215)},
}


# TODO: DIVIDE AREAS INTO SEPARATE FRAMES
# TODO: IMPLEMENT config.py
class GUI(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master        
        master.title("Cafe POS Database Management")
        master.geometry("600x475")
        master['bg'] = COLORS['light_steel_blue']['py_name']        
        self.selected_item = 0        
        self.create_widgets()
        self.create_buttons()
        self.populate_list()

    def create_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam") # default, clam, alt
        '''
        style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3)
        style.map("Treeview", background=[("selected", "blue")])
        '''

    def create_frames(self):
        """Create GUI Frames
        """
        # INSTANTIATE FRAMES
        self.frame_left_full = tk.Frame(master=self.master)
        self.frame_right_full = tk.Frame(master=self.master)
        self.frame_left_top_child = tk.Frame(master=self.frame_left_full)
        self.frame_left_bottom_child = tk.Frame(master=self.frame_left_full)
        self.frame_search = tk.LabelFrame(master=self.frame_left_top_child, text="SEARCH")
        # RENDER/PACK FRAMES
        self.frame_left_full.pack(fill="both", expand=True, side=tk.LEFT, anchor=tk.W)
        self.frame_right_full.pack(fill="both", expand=True, side=tk.RIGHT, anchor=tk.E)
        self.frame_left_top_child.pack(fill="both", expand=True, side=tk.TOP, anchor=tk.NW)
        self.frame_left_bottom_child.pack(fill="both", expand=True, side=tk.BOTTOM, anchor=tk.SW)
        self.frame_search.pack(fill="both", expand=True, side=tk.BOTTOM, anchor=tk.WSE)

    def create_widgets(self):
        """Create GUI Widgets
        """
        # ID WIDGET
        self.id_text = tk.StringVar()
        self.id_label = tk.Label(
            self.master, text=lf_.TXT[0].upper(), cnf=lf_.cnf)
        self.id_label.grid(row=0, cnf=lf_.cnf_grid)
        self.id_entry = tk.Entry(self.master, textvariable=self.id_text)
        self.id_entry.grid(row=0, cnf=if_.cnf_grid)

        # CATEGORY WIDGET
        self.category_text = tk.StringVar()
        self.category_label = tk.Label(
            self.master, text=lf_.TXT[1].upper(), cnf=lf_.cnf)
        self.category_label.grid(row=1, cnf=lf_.cnf_grid)
        self.category_entry = tk.Entry(
            self.master, textvariable=self.category_text)
        self.category_entry.grid(row=1, cnf=if_.cnf_grid)

        # NAME WIDGET
        self.name_text = tk.StringVar()
        self.name_label = tk.Label(
            self.master, text=lf_.TXT[2].upper(), cnf=lf_.cnf)
        self.name_label.grid(row=2, cnf=lf_.cnf_grid)
        self.name_entry = tk.Entry(
            self.master, textvariable=self.name_text)
        self.name_entry.grid(row=2, cnf=if_.cnf_grid)

        # POS LABEL WIDGET
        self.pos_label_text = tk.StringVar()
        self.pos_label_label = tk.Label(
            self.master, text=lf_.TXT[3].upper(), cnf=lf_.cnf)
        self.pos_label_label.grid(row=3, cnf=lf_.cnf_grid)
        self.pos_label_entry = tk.Entry(
            self.master, textvariable=self.pos_label_text)
        self.pos_label_entry.grid(row=3, cnf=if_.cnf_grid)

        # PRICE WIDGET
        self.price_text = tk.StringVar()
        self.price_label = tk.Label(
            self.master, text=lf_.TXT[4].upper(), cnf=lf_.cnf)
        self.price_label.grid(row=4, cnf=lf_.cnf_grid)
        self.price_entry = tk.Entry(self.master, textvariable=self.price_text)
        self.price_entry.grid(row=4, cnf=if_.cnf_grid)

        # SEARCH WIDGET
        self.search_text = tk.StringVar()
        self.search_label = tk.Label(
            self.master, text=lf_.TXT[5].upper(), cnf=lf_.cnf)
        self.search_label.grid(row=5, cnf=lf_.cnf_grid)
        self.search_entry = tk.Entry(self.master, textvariable=self.search_text)
        self.search_entry.grid(row=5, cnf=if_.cnf_grid)
        
        # LISTBOX -> replacing with TreeView
        self.create_listbox()
        # self.create_treeview()

    def create_treeview(self):
        """Create TreeView GUI widget
        """
        self.tree_view = ttk.Treeview(self.master, columns=tv_.columns, show=tv_.show, selectmode=tv_.selectmode)
        self.tree_view.pack()
        
        self.tree_view.heading(1, text=tv_.HEADINGS[0])
        self.tree_view.heading(2, text=tv_.HEADINGS[1])
        self.tree_view.heading(3, text=tv_.HEADINGS[2])
        self.tree_view.heading(4, text=tv_.HEADINGS[3])
        self.tree_view.heading(5, text=tv_.HEADINGS[4])
        
        self.vsb = ttk.Scrollbar(orient="vertical", command=self.tree_view.yview)
        self.hsb = ttk.Scrollbar(orient="horizontal", command=self.tree_view.xview)
        self.tree_view.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        self.tree_view.grid(column=0, row=0, sticky='nsew', in_=container)
        self.vsb.grid(column=1, row=0, sticky='ns', in_=container)
        self.hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        
        self.tree_view.bind(lb_.bind_seq, self.select_item)

    def create_listbox(self):
        """Create ListBox GUI widget
        """
        # ITEMS LIST -> listbox
        self.items_list = tk.Listbox(self.master, cnf=lb_.cnf)
        self.items_list.grid(cnf=lb_.cnf_grid)

        # SCROLLBAR WIDGET
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(cnf=bs_.cnf_grid)

        # SET SCROLLBAR WIDGET
        self.items_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.items_list.yview)

        # BIND LISTBOX SELECTION
        self.items_list.bind(lb_.bind_seq, self.select_item)

    def create_buttons(self):
        """Add button widgets to frame(s) -> ADD, REMOVE, UPDATE, CLEAR, SEARCH, ...
        """
        # ADD
        self.add_btn = tk.Button(
            master=self.master, text=b_.TXT[0].upper(), command=self.add_item, cnf=b_.cnf)
        self.add_btn.grid(row=0, column=2, cnf=b_.cnf_grid)
        # REMOVE
        self.remove_btn = tk.Button(
            master=self.master, text=b_.TXT[1].upper(), command=self.remove_item, cnf=b_.cnf)
        self.remove_btn.grid(row=0, column=3, cnf=b_.cnf_grid)
        # UPDATE
        self.update_btn = tk.Button(
            master=self.master, text=b_.TXT[2].upper(), command=self.update_item, cnf=b_.cnf)
        self.update_btn.grid(row=1, column=2, cnf=b_.cnf_grid)
        # CLEAR
        self.clear_btn = tk.Button(
            master=self.master, text=b_.TXT[3].upper(), command=self.clear_text, cnf=b_.cnf)
        self.clear_btn.grid(row=1, column=3, cnf=b_.cnf_grid)
        # IMPORT CSV
        self.import_csv_btn = tk.Button(
            master=self.master, text=b_.TXT[4].upper(), command=lambda: print(f"{b_.TXT[4].upper()} Clicked!"), cnf=b_.cnf)
        self.import_csv_btn.grid(row=2, column=2, cnf=b_.cnf_grid)
        # EXPORT CSV
        self.export_csv_btn = tk.Button(
            master=self.master, text=b_.TXT[5].upper(), command=lambda: print(f"{b_.TXT[5].upper()} Clicked!"), cnf=b_.cnf)
        self.export_csv_btn.grid(row=2, column=3, cnf=b_.cnf_grid)
        # IMPORT JSON
        self.import_json_btn = tk.Button(
            master=self.master, text=b_.TXT[6].upper(), command=lambda: print(f"{b_.TXT[6].upper()} Clicked!"), cnf=b_.cnf)
        self.import_json_btn.grid(row=3, column=2, cnf=b_.cnf_grid)
        # EXPORT JSON
        self.export_json_btn = tk.Button(
            master=self.master, text=b_.TXT[7].upper(), command=lambda: print(f"{b_.TXT[7].upper()} Clicked!"), cnf=b_.cnf)
        self.export_json_btn.grid(row=3, column=3, cnf=b_.cnf_grid)
        # IMPORT DUMP
        self.import_dump_btn = tk.Button(
            master=self.master, text=b_.TXT[8].upper(), command=lambda: print(f"{b_.TXT[8].upper()} Clicked!"), cnf=b_.cnf)
        self.import_dump_btn.grid(row=4, column=2, cnf=b_.cnf_grid)
        # EXPORT DUMP
        self.export_dump_btn = tk.Button(
            master=self.master, text=b_.TXT[9].upper(), command=lambda: print(f"{b_.TXT[9].upper()} Clicked!"), cnf=b_.cnf)
        self.export_dump_btn.grid(row=4, column=3, cnf=b_.cnf_grid)
        # SEARCH
        self.search_btn = tk.Button(
            master=self.master, text=b_.TXT[10].upper(), command=self.search_item_id, cnf=b_.cnf)
        self.search_btn.grid(row=5, column=2, cnf=b_.cnf_grid)
        # POPULATE [Reload] LIST
        self.populate_btn = tk.Button(
            master=self.master, text=b_.TXT[11].upper(), command=self.populate_list, cnf=b_.cnf)
        self.populate_btn.grid(row=5, column=3, cnf=b_.cnf_grid)

    def populate_list(self):
        """Populate ListBox GUI widget with dataset
        """
        self.clear_text()
        self.items_list.delete(0, tk.END)
        for row in db.fetch_all():
            self.items_list.insert(tk.END, row)

    # TODO: NOT IMPLEMENTED YET
    def populate_tree(self):
        self.clear_text()
        self.tree_view.delete(*self.tree_view.get_children())
        for row in db.fetch_all():
            self.tree_view.insert("", "end", values=row)

    def add_item(self):
        """Add item (record) into database and ListBox widget
        """
        new_item = {
            "id_": self.id_text.get().upper(),
            "category_": self.category_text.get().lower(),
            "name_": self.name_text.get().capitalize(),
            "pos_label_": self.pos_label_text.get().upper(),
            "price_": float(self.price_text.get()),
        }
        
        conditions = [
            new_item['id_'] == '',
            new_item['category_'] == '',
            new_item['name_'] == '',
            new_item['pos_label_'] == '',
            new_item['price_'] == ''
        ]
        if any(conditions):
            messagebox.showerror(mb_.ERRORS['add_item']['title'], mb_.ERRORS['add_item']['message'])
            return
        print(self.id_text.get())
        
        db.insert(
            new_item['id_'], new_item['category_'], new_item['name_'], new_item['pos_label_'], new_item['price_'])
        self.items_list.delete(0, tk.END)
        # FIXME: is this redundant?? -> populate_list() called immediately after
        self.items_list.insert(tk.END, (
            new_item['id_'], new_item['category_'], new_item['name_'], new_item['pos_label_'], new_item['price_']))
        # self.clear_text()
        self.populate_list()

    def select_item(self, event):
        """Insert selected item (record) into respective text fields

        Args:
            event ([type]): [description]
        """
        # Global selected item for use in other functions
        # global self.selected_item
        try:
            index = self.items_list.curselection()[0]
            self.selected_item = self.items_list.get(index)

            # DEBUG ===================
            print(self.selected_item)
            # =========================

            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(tk.END, self.selected_item[0])
            self.category_entry.delete(0, tk.END)
            self.category_entry.insert(tk.END, self.selected_item[1])
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, self.selected_item[2])
            self.pos_label_entry.delete(0, tk.END)
            self.pos_label_entry.insert(tk.END, self.selected_item[3])
            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(tk.END, self.selected_item[4])
        except IndexError:
            pass

    def remove_item(self):
        """Remove item (record)
        """
        if messagebox.askyesno(title=m_.DELETE['title'], message=f"{m_.DELETE['message']} {self.selected_item[0]}"):
            db.remove(self.selected_item[0])
            # self.clear_text()
            self.populate_list()

    def update_item(self):
        """Update item (record)
        """
        if messagebox.askyesno(title=m_.UPDATE['title'], message=f"{m_.UPDATE['message']} {self.selected_item[0]}"):
            db.update(
                self.selected_item[0],
                self.category_text.get().lower(),
                self.name_text.get().capitalize(),
                self.pos_label_text.get().upper(),
                float(self.price_text.get())
            )
            # self.clear_text()
            self.populate_list()

    def clear_text(self):
        """Clear text fields
        """
        self.id_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.pos_label_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)

    def search_item_id(self):
        """Search by item ID
        """
        self.items_list.delete(0, tk.END)
        for row in db.search(self.search_text.get().upper()):
            self.items_list.insert(tk.END, row)
            
        ''' SEARCH ITEMS Treeview ----------------------------
        tree_view.delete(*tree_view.get_children())
        for row in db.search(self.search_text.get().upper()):
            tree_view.insert("", "end", values=row)
        ---------------------------------------------------'''

def main():
    root = tk.Tk()
    root.minsize(width=600, height=450)
    gui = GUI(master=root)
    gui.mainloop()


if __name__ == '__main__':
    main()
