import sqlite3

DB_NAME = "database.db"

def init_db():
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()

    # USERS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT DEFAULT 'user'
    )
    """)

    # WATCHLIST TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS watchlist (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        coin_id TEXT,
        UNIQUE(user_id, coin_id)
    )
    """)

    db.commit()
    db.close()

    print("Database initialized successfully")
