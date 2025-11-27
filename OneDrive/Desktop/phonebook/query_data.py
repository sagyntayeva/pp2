from connect import connect

def query_data():
    filter_name = input("Введите имя для поиска (или оставьте пустым): ")
    
    conn = connect()
    cur = conn.cursor()

    if filter_name:
        cur.execute("SELECT * FROM PhoneBook WHERE first_name = %s", (filter_name,))
    else:
        cur.execute("SELECT * FROM PhoneBook")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

query_data()

