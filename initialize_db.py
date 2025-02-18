import sqlite3

def initialize_database():
    """Initialize the SQLite database with the necessary tables."""
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    # Create the books table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL
        )
    ''')

    # Create the passages table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            text TEXT NOT NULL,
            chapter TEXT,
            page INTEGER,
            FOREIGN KEY (book_id) REFERENCES books (id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully!")
