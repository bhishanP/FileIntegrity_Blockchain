import sqlite3

DB_NAME = "blockchain.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS blocks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        idx INTEGER,
        timestamp REAL,
        merkle_root TEXT,
        previous_hash TEXT
    )
    """)

    conn.commit()
    conn.close()