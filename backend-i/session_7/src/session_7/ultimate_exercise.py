import sqlite3
from contextlib import contextmanager

@contextmanager
def database():
    conn = sqlite3.connect('example.db')
    try:
        cursor = conn.cursor()
        yield cursor
    finally:
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='accounts'")
        result = cursor.fetchone()
        if result:
            print("Table 'accounts' already exists.")
        else:
      
            cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                                user TEXT,
                                email TEXT,
                                password TEXT)''')
   
            cursor.execute("INSERT INTO accounts (user, email, password) VALUES ('goncas','ola@troll.com','RHAT')")
            conn.commit() 

        conn.close() 

# Exemplo de uso
if __name__ == "__main__":
    with database() as cursor:

        cursor.execute("SELECT * FROM accounts")
        for row in cursor.fetchall():
            print(row)
