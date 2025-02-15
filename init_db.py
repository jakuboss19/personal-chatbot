import sqlite3
import logging

#configure logging
logging.basicConfig(level=logging.INFO)

def create_database():
    try:
        conn = sqlite3.connect("books.db")
        cursor = conn.cursor()

        create_books_table(cursor)
        create_passages_table(cursor)

        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
    
# Create table for books
def create_books_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        year INTEGER
    )
    """)
    
# Create table for passages
def create_passages_table(cursor):
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

    logging.info("Passages table created successfully!")


if __name__ == "__main__":
    create_database()
