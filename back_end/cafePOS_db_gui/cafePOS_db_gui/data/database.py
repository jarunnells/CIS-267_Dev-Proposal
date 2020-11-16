import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS items (id TEXT PRIMARY KEY, category TEXT NOT NULL, name TEXT NOT NULL, label TEXT NOT NULL, price REAL NOT NULL)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM items")
        rows = self.cur.fetchall()
        return rows

    def insert(self, id, category, name, label, price):
        self.cur.execute("INSERT INTO items VALUES (?, ?, ?, ?, ?)",
                         (id, category, name, label, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM items WHERE id = ?", (id,))
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE items SET id = ?, category = ?, name = ?, label = ?, price = ? WHERE id = ?",
                         (id, part, customer, retailer, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# db = Database(':memory:')
# db.insert('BK001', 'bkfast', 'Muffin', 'MUFFIN', 2.75)
# db.insert('HB001', 'bev_hot', 'Coffee', 'COFFEE', 1.99)
# db.insert('CB001', 'bev_cold', 'Aquafina', 'AQUA H20', 1.00)
# db.insert('DE001', 'deli', 'Noodle Cup', 'NOODLE CUP', 1.00)
# db.insert('SN001', 'snack', 'House Cookie', 'HOUSE COOKIE', 1.64)
# db.insert('CD001', 'condiment', 'Dressing', 'DRESSING', 0.75)