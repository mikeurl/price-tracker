import sqlite3

def create_table():
    conn = sqlite3.connect('prices.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS prices (id INTEGER PRIMARY KEY, url TEXT, price TEXT)''')
    conn.commit()
    conn.close()

def insert_price(url, price):
    conn = sqlite3.connect('prices.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO prices (url, price) VALUES (?, ?)', (url, price))
    conn.commit()
    conn.close()

def get_prices():
    conn = sqlite3.connect('prices.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM prices')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Example usage
if __name__ == "__main__":
    create_table()
    insert_price('http://example.com/product', '$19.99')
    prices = get_prices()
    for row in prices:
        print(row)
