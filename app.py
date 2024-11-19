import json

def load_books():
    """Nacte knihy ulozene v json souborech"""
    try:
        with open("books.json", "r", encoding="utf-8") as f:
            books = json.load(f)
        print("Knihy nacteny")
        return books
    except FileNotFoundError:
        print("Soubor s knihami nenalezen.")
        return []

def search_books(books, query):
    """Vyhleda pasaze z knih na zaklade dotazu"""
    results = []
    for book in books:
        for passage in book["passages"]:
            if query.lower() in passage["text"].lower():
                results.append({"book": book["title"], "text": passage["text"]})
    return results

def main():
    """Hlavni funkce"""
    books = load_books()
    print("\nVítejte v chatovacím systému s knihami!")
    
    while True:
        query = input("\nZadejte otázku nebo 'exit' pro ukončení: ")
        if query.lower() == "exit":
            print("Děkujeme za použití aplikace!")
            break
        
        results = search_books(books, query)
        if results:
            print("\nNalezené pasáže:")
            for result in results:
                print(f"\nZ knihy: {result['book']}\n{result['text']}")
        else:
            print("\nŽádné výsledky nenalezeny.")

if __name__ == "__main__":
    main()
