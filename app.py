import sqlite3

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

def search_books(query, search_in="text", case_sensitive=False):
    """
    Search books and passages directly in databaase
    query: Search request
    case_sensitive: IF False, not case sensitive
    """
    conn = sqlite.connect("books.db")
    cursor = conn.cursor()

    sql = f"""
        SELECT books.title, books.author, books.year, passages.text, passages.chapter, passages.page 
        FROM books
        JOIN passages ON books.id = passages.book_id
        WHERE {search_in} LIKE ?
    """

    if not case_sensitive:
        query = query.lower()
        sql = f"""
            SELECT books.title, books.author, books.year, passages.text, passages.chapter, passages.page 
            FROM books
            JOIN passages ON books.id = passages.book_id
            WHERE LOWER({search_in}) LIKE ?
        """

    cursor.execue(sql, (f"%{query}%",))
    results = cursor.fetchall()
    conn.close()
    return [
        {"title": row[0], "author": row[1], "year": row[2], "text": row[3], "chapter": row[4], "page": row[5]}
        for row in results
    ]

def main():
    books = load_books()
    print("\nVítejte v chatovacím systému s databází knih!")
    
    while True:
        query = input("\nZadejte otázku nebo 'exit' pro ukončení: ")
        if query.lower() == "exit":
            print("Děkujeme za použití aplikace!")
            break
        
        results = search_books(query)
        if results:
            print("\nNalezené pasáže:")
            for result in results:
                print(f"\nZ knihy: {result['title']} (Kapitola: {result['chapter']}, Strana: {result['page']})")
                print(f"Text: {result['text']}")
        else:
            print("\nŽádné výsledky nenalezeny.")

if __name__ == "__main__":
    main()
