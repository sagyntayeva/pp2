import psycopg2
from connect import connect

def create_tables():
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1
        );
    """)
    
    conn.commit()
    cur.close()
    conn.close()

create_tables()
#python Snake.py
#psql -U postgres -d phonebook
# SELECT * FROM users;
#SELECT * FROM user_score;