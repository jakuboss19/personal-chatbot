import sqlite3
import re

def load_books():
    """Load books and passages from db"""
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT b.title, b.author, b.year, p.text, p.chapter, p.page
    FROM books b
    JOIN passages p ON b.id = p.book_id
    """)
    rows = cursor.fetchall()
    conn.close()

    books = []
    for row in rows:
        books.append({
            "title": row[0],
            "author": row[1],
            "year": row[2],
            "text": row[3],
            "chapter": row[4],
            "page": row[5]
        })
    return books

def search_books(books, query, search_in="text", case_sensitive=False):
    """
    Search books and passages
    :param query: Search request
    :param case_sensitive: IF False, not case sensitive
    :return: List of searched passages
    """
    results = []
    for book in books:
        if search_in not in book:
            continue  # IF not searched, continue

        text_to_search = book[search_in]
        if not case_sensitive:
            text_to_search = text_to_search.lower()
            query = query.lower()

        if query in text_to_search:
            results.append(book)
    return results

def main():
    books = load_books()
    print("\nVítejte v chatovacím systému s databází knih!")
    
    while True:
        query = input("\nZadejte otázku nebo 'exit' pro ukončení: ")
        if query.lower() == "exit":
            print("Děkujeme za použití aplikace!")
            break
        
        results = search_books(books, query)
        if results:
            print("\nNalezené pasáže:")
            for result in results:
                print(f"\nZ knihy: {result['title']} (Kapitola: {result['chapter']}, Strana: {result['page']})")
                print(f"Text: {result['text']}")
        else:
            print("\nŽádné výsledky nenalezeny.")

if __name__ == "__main__":
    main()
