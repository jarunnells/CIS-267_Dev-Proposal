# SYSTEM IMPORTS
# try:
#     import tkinter as tk
# except ImportError:
#     import Tkinter as tk
# from tkinter import messagebox

# CUSTOM IMPORTS
# from modules.DBManager import DBManager

# class GUI(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#         self.master = master
#         master.title("Cafe POS Database")
#         master.geometry("800x450")

#         self.create_widgets()
#         self.item_selected = 0
#         self.populate_items()

#     def create_widgets(self):
#         self.add_btn = tk.Button(
#             self.master, text="Add Part", width=12, command=lambda: print("btn clicked!"))
#         self.add_btn.grid(row=2, column=0, pady=20)
#         print("Widgets created!")

#     def populate_items(self):
#         print("Items populated!")

# if __name__ == '__main__':
#     root = tk.Tk()
#     gui = GUI(master=root)
#     gui.mainloop()


# ================================================================================================

# STANDARD LIBRARY IMPORTS
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from tkinter import messagebox

# CUSTOM LIBRARY IMPORTS
# from modules.DBManager import DBManager
from data.database import Database

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


class GUI(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title("Cafe POS Database Management")
        master.geometry("700x425")
        master['bg'] = COLORS['light_steel_blue']['py_name']
        self.create_widgets()
        self.render_buttons()
        self.selected_item = 0
        self.populate_list()

    def create_widgets(self):
        # ID
        self.id_text = tk.StringVar()
        self.id_label = tk.Label(
            self.master, text=TXT[0][0].upper(), font=("bold", 14), padx=0, pady=0)
        self.id_label.grid(row=0, column=0, sticky=tk.W)
        self.id_entry = tk.Entry(self.master, textvariable=self.id_text)
        self.id_entry.grid(row=0, column=1)

        # CATEGORY
        self.category_text = tk.StringVar()
        self.category_label = tk.Label(
            self.master, text=TXT[0][1].upper(), font=("bold", 14), padx=0, pady=0)
        self.category_label.grid(row=1, column=0, sticky=tk.W)
        self.category_entry = tk.Entry(
            self.master, textvariable=self.category_text)
        self.category_entry.grid(row=1, column=1)

        # NAME
        self.name_text = tk.StringVar()
        self.name_label = tk.Label(
            self.master, text=TXT[0][2].upper(), font=("bold", 14), padx=0, pady=0)
        self.name_label.grid(row=2, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(
            self.master, textvariable=self.name_text)
        self.name_entry.grid(row=2, column=1)

        # POS LABEL
        self.pos_label_text = tk.StringVar()
        self.pos_label_label = tk.Label(
            self.master, text=TXT[0][3].upper(), font=("bold", 14), padx=0, pady=0)
        self.pos_label_label.grid(row=3, column=0, sticky=tk.W)
        self.pos_label_entry = tk.Entry(
            self.master, textvariable=self.pos_label_text)
        self.pos_label_entry.grid(row=3, column=1)

        # PRICE
        self.price_text = tk.StringVar()
        self.price_label = tk.Label(
            self.master, text=TXT[0][4].upper(), font=("bold", 14), pady=0)
        self.price_label.grid(row=4, column=0, sticky=tk.W)
        self.price_entry = tk.Entry(self.master, textvariable=self.price_text)
        self.price_entry.grid(row=4, column=1)

        # ITEMS LIST -> listbox
        self.items_list = tk.Listbox(self.master, height=8, width=50, border=0)
        self.items_list.grid(
            row=6, column=0, columnspan=3, rowspan=6, pady=20, padx=20
        )

        # SCROLLBAR
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=6, column=3)

        # Set scrollbar to parts
        self.items_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.items_list.yview)

        # BIND SELECT
        self.items_list.bind('<<ListboxSelect>>', self.select_item)

    def render_buttons(self):
        # ADD ITEM BUTTON
        self.add_btn = tk.Button(
            self.master, text=TXT[1][0].upper(), width=12, command=self.add_item)
        self.add_btn.grid(row=0, column=2, padx=0, pady=0)

        # REMOVE ITEM BUTTON
        self.remove_btn = tk.Button(
            self.master, text=TXT[1][1].upper(), width=12, command=self.remove_item)
        self.remove_btn.grid(row=0, column=3, padx=0, pady=0)

        # UPDATE ITEM BUTTON
        self.update_btn = tk.Button(
            self.master, text=TXT[1][2].upper(), width=12, command=self.update_item)
        self.update_btn.grid(row=1, column=2, padx=0, pady=0)

        # CLEAR INPUT FIELDS BUTTON
        self.clear_btn = tk.Button(
            self.master, text=TXT[1][3].upper(), width=12, command=self.clear_text)
        self.clear_btn.grid(row=1, column=3, padx=0, pady=0)

    def populate_list(self):
        self.items_list.delete(0, tk.END)
        for row in db.fetch():
            self.items_list.insert(tk.END, row)

    def add_item(self):
        conditions = [
            self.id_text.get() == '',
            self.category_text.get() == '',
            self.name_text.get() == '',
            self.pos_label_text.get() == ''
        ]
        if any(conditions):
            messagebox.showerror(ERRORS['title'], ERRORS['message'])
            return
        print(self.id_text.get())
        db.insert(
            self.id_text.get(), self.category_text.get(), self.name_text.get(), self.pos_label_text.get())
        self.items_list.delete(0, tk.END)
        self.items_list.insert(tk.END, (self.id_text.get(), self.category_text.get(
        ), self.name_text.get(), self.pos_label_text.get()))
        self.clear_text()
        self.populate_list()

    def select_item(self, event):
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

    # Remove item
    def remove_item(self):
        db.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()

    # Update item
    def update_item(self):
        db.update(
            self.selected_item[0],
            self.category_text.get(),
            self.name_text.get(),
            self.pos_label_text.get(),
            self.price_text.get()
        )
        self.populate_list()

    # Clear all text fields
    def clear_text(self):
        self.id_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.pos_label_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    gui = GUI(master=root)
    gui.mainloop()
