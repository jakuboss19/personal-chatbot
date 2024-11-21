import sqlite3

def add_books():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    # Přidání knihy
    cursor.execute("""
    INSERT INTO books (title, author, year) VALUES
    ("Book 1", "Author 1", 2021),
    ("Book 2", "Author 2", 2020)
    """)

    # Přidání pasáží
    cursor.execute("""
    INSERT INTO passages (book_id, text, chapter, page) VALUES
    (1, "This is the first passage.", "Introduction", 1),
    (1, "Another key insight.", "Chapter 1", 5),
    (2, "A passage from Book 2.", "Prologue", 2)
    """)

    conn.commit()
    conn.close()
    print("Books and passages added successfully!")

if __name__ == "__main__":
    add_books()
