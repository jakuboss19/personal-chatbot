import sqlite3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def get_db_connection():
    """Establish a database connection"""
    try:
        conn = sqlite3.connect("books.db")
        return conn
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database: {e}")
        return None

def load_books():
    """Load books and passages from db"""
    conn = get_db_connection()
    if conn is None:
        return []
    
    cursor = conn.cursor()
    cursor.execute("""
    SELECT b.title, b.author, b.year, p.text, p.chapter, p.page
    FROM books b
    JOIN passages p ON b.id = p.book_id
    """)
    rows = cursor.fetchall()
    conn.close()

    books = [
        {
            "title": row[0],
            "author": row[1],
            "year": row[2],
            "text": row[3],
            "chapter": row[4],
            "page": row[5]
        }
        for row in rows
    ]
    return books

def search_books(query, search_in="text", case_sensitive=False):
    """
    Search books and passages directly in database
    query: Search request
    case_sensitive: IF False, not case sensitive
    """
    conn = get_db_connection()
    if conn is None:
        return []
    
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
            WHERE LOWER({search_in}) LIKE LOWER(?)
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
