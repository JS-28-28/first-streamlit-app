import sqlite3
import os

DB_FILE = "book.db"

def get_connection():
    # If the database doesn't exist, create it and the tables
    first_time = not os.path.exists(DB_FILE)
    conn = sqlite3.connect(DB_FILE)
    if first_time:
        create_tables(conn)
    return conn

def create_tables(conn):
    cursor = conn.cursor()
    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            user_type TEXT
        )
    """)
    conn.commit()
