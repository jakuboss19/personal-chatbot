import sqlite3

def init_db():
     """Initialize the database and create tables."""
    try:
        with sqlite3.connect("books.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS passages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER,
                text TEXT NOT NULL,
                chapter TEXT,
                page INTEGER,
                FOREIGN KEY(book_id) REFERENCES books(id)
            )
            """)
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def insert_books(books):
    """insert books into sql"""
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", books)
    conn.commit()
    conn.close()

def insert_passages(passages):
    """insert passages into sql"""
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO passages (book_id, text, chapter, page) VALUES (?, ?, ?, ?)", passages)
    conn.commit()
    conn.close()

def add_sample_data():
    """add data about books and passages"""
    books = [
        ("Book 1", "Author 1", 2021),
        ("Book 2", "Author 2", 2020)
    ]
    passages = [
        (1, "This is the first passage.", "Introduction", 1),
        (1, "Another key insight.", "Chapter 1", 5),
        (2, "A passage from Book 2.", "Prologue", 2)
    ]

    insert_books(books)
    insert_passages(passages)
    print("Sample data added successfully!")

if __name__ == "__main__":
    init_db()
    add_sample_data()
