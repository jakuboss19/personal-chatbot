import sqlite3

def create_database():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    # Vytvoření tabulky pro knihy
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        year INTEGER
    )
    """)

    # Vytvoření tabulky pro pasáže
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS passages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        text TEXT NOT NULL,
        chapter TEXT,
        page INTEGER,
        FOREIGN KEY (book_id) REFERENCES books (id)
    )
    """)

    conn.commit()
    conn.close()
    print("Database and tables created successfully!")

if __name__ == "__main__":
    create_database()
