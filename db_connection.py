import sqlite3
import os

DB_FILE = "book.db"

def get_connection():
    """Return a SQLite connection. Creates DB and tables if first time."""
    first_time = not os.path.exists(DB_FILE)
    conn = sqlite3.connect(DB_FILE)
    if first_time:
        create_tables(conn)
    return conn

def create_tables(conn):
    """Create users, donations, and requests tables."""
    cursor = conn.cursor()

    # ---------- users table ----------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        user_type TEXT
    )
    """)

    # ---------- donations table ----------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS donations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        donor_name TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        donor_type TEXT,
        book_title TEXT NOT NULL,
        author TEXT,
        genre TEXT,
        condition_status TEXT,
        donation_date TEXT,
        book_image TEXT
    )
    """)

    # ---------- requests table ----------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        book_id INTEGER NOT NULL,
        request_date TEXT DEFAULT (datetime('now')),
        FOREIGN KEY (book_id) REFERENCES donations(id)
    )
    """)

    conn.commit()
