import psycopg2

conn = psycopg2.connect(
    dbname="phonebook_db",
    user="phonebook_user",
    password="password",
    host="localhost",
    port="5432"
)
print("Connected!")
conn.close()
