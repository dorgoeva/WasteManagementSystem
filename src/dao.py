import sqlite3

class WasteDAO:
    def __init__(self):
        self.conn = sqlite3.connect('database/waste_mgmt.db')

    def create_tables(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS requests
                     (id INTEGER PRIMARY KEY, name TEXT, type TEXT, date TEXT)''')
        self.conn.commit()
