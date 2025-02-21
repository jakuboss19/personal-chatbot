import sqlite3
from extract_text import extract_text_from_pdf

#script for frontend

def insert_book(title, author, year):
    """Insert a book into the database."""
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()
    book_id = cursor.lastrowid
    conn.close()
    return book_id

def insert_passages(passages):
    """Insert passages into the database."""
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO passages (book_id, text, chapter, page) VALUES (?, ?, ?, ?)", passages)
    conn.commit()
    conn.close()

# Example usage
book_id = insert_book("Sample Book Title", "Author Name", 2023)
chapter = "Chapter 1"  # Replace with the actual chapter
page = 1  # Replace with the actual page number

# Assuming `text` is extracted from the PDF
text = extract_text_from_pdf('maj.pdf')

# Split the text into passages (this is a simple example)
passages = [(book_id, text_segment, chapter, page) for text_segment in text.split('\n\n') if text_segment.strip()]

insert_passages(passages)
print("Passages added successfully!")
