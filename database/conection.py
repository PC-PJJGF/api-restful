import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()  # Un cursor es un puntero que nos permite ejecutar sentencias SQL sobre la base de datos.
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, name TEXT, email TEXT, phone TEXT, address TEXT)")
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()
    
    def get_user(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def add_user(self, username, password, name, email, phone, address):
        self.cursor.execute("INSERT INTO users (username, password, name, email, phone, address) VALUES (?, ?, ?, ?, ?, ?)", (username, password, name, email, phone, address))
        self.connection.commit()

    def delete_user(self, username, email):
        try:
            self.cursor.execute("DELETE FROM users WHERE username = ? AND email = ?", (username, email))
            self.connection.commit()
        except sqlite3.OperationalError:
            pass
    
    def update_user(self, username, password, name, email, phone, address):
        self.cursor.execute("UPDATE users SET password = ?, name = ?, email = ?, phone = ?, address = ? WHERE username = ?", (password, name, email, phone, address, username))
        self.connection.commit()
        