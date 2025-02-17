from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/books', methods=['GET'])
def get_books():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return jsonify([dict(row) for row in books])

@app.route('/api/search', methods=['GET'])
def search_books():
    query = request.args.get('q')
    conn = get_db_connection()
    results = conn.execute(
        'SELECT * FROM books JOIN passages ON books.id = passages.book_id WHERE text LIKE ?',
        (f'%{query}%',)
    ).fetchall()
    conn.close()
    return jsonify([dict(row) for row in results])

if __name__ == '__main__':
    app.run(debug=True)
