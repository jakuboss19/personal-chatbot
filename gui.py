import tkinter as tk
from tkinter import ttk
import sqlite3

def search_passages(query):
    """Search books and passages directly in the database."""
    try:
        with sqlite3.connect("books.db") as conn: 
            cursor = conn.cursor()
            cursor.execute("""
                SELECT books.title, books.author, books.year, passages.text, passages.chapter, passages.page 
                FROM books
                JOIN passages ON books.id = passages.book_id
                WHERE books.title LIKE ? OR books.author LIKE ? OR passages.text LIKE ?
            """, (f"%{query}%", f"%{query}%", f"%{query}%"))
            results = cursor.fetchall()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    return results

def perform_search():
    """Gets input from search field and updates the results table."""
    query = search_entry.get().strip()
    if query:
        results = search_passages(query)
        # Clear previous search results
        for row in results_tree.get_children():
            results_tree.delete(row)
        # Insert new search results
        for result in results:
            results_tree.insert("", tk.END, values=result)
    else:
        messagebox.showinfo("Input Required", "Please enter a search query")
        
def setup_ui():
    """setup ui components"""
    
    # Create main window
    root = tk.Tk()
    root.title("Book Search")

    # Search bar
    search_frame = ttk.Frame(root)
    search_frame.pack(pady=10, padx=10, fill="x")

    ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT, padx=5)
    search_entry = ttk.Entry(search_frame, width=50)
    search_entry.pack(side=tk.LEFT, padx=5, expand=True, fill="x")

    search_button = ttk.Button(search_frame, text="Search", command=perform_search)
    search_button.pack(side=tk.LEFT, padx=5)

    # Results table
    columns = ("Title", "Author", "Year", "Passage", "Chapter", "Page")
    results_tree = ttk.Treeview(root, columns=columns, show="headings")

    for col in columns:
        results_tree.heading(col, text=col)
        results_tree.column(col, width=tkFont.Font().measure(col) + 20)

    results_tree.pack(padx=10, pady=10, fill="both", expand=True)
    return root, search_entry, results_tree

# Run GUI loop

if __name__ == "__main__":
    root, search_entry, results_tree = setup_ui()
    root.mainloop()
