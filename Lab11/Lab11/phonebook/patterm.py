
from connect import connect
def search(pattern):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM PhoneBook
        WHERE first_name LIKE %s OR phone LIKE %s
    """, ('%' + pattern + '%', '%' + pattern + '%'))
    
    results = cur.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("Нет совпадений")
    
    cur.close()
    conn.close()

search('Aidos')