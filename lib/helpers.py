#helpers.py
import sqlite3

DB_NAME = "hotel.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL CHECK(length(phone) >= 10)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            visit_date DATE NOT NULL,
            amount_paid REAL NOT NULL CHECK(amount_paid >= 0),
            FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
        );
    """)
    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect(DB_NAME)
