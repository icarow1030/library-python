import sqlite3
import os
import pandas as pd

data_path = "data/library.db"

if not os.path.exists("data"):
    os.makedirs("data")
    

def create_table():
    conn = sqlite3.connect(data_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        Autor TEXT NOT NULL,
        ano_lancamento INTEGER,
        preco FLOAT
    )
    ''')
    conn.commit()
    conn.close()
    
create_table()

def add_book(title, author, published_year, price):
    conn = sqlite3.connect(data_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books (titulo, autor, ano_lancamento, preco)
        VALUES (?, ?, ?, ?)
    ''', (title, author, published_year, price))
    conn.commit()
    conn.close()
    

def show_all_books():
    conn = sqlite3.connect(data_path)
    query = 'SELECT * FROM books'
    tabela = pd.read_sql_query(query, conn)
    return tabela.values.tolist()
    


def update_price(id, new_price):
    conn = sqlite3.connect(data_path)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE books
        SET preco = ?
        WHERE id = ?
    ''', (new_price, id))
    conn.commit()
    conn.close()
    

def remove_book(id):
    conn = sqlite3.connect(data_path)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM books
        WHERE id = ?
    ''', (id,))
    conn.commit()
    conn.close()
    
    
def search_book_by_author(author):
    conn = sqlite3.connect(data_path)
    query = f"SELECT * FROM books where autor ='{author}' "
    tabela = pd.read_sql_query(query, conn)
    print(tabela)