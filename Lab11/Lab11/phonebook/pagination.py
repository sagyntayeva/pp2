
from connect import connect

def paginated(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM PhoneBook LIMIT %s OFFSET %s", (limit, offset)) 
    rows = cur.fetchall()
    
    if not rows:
        print("Нет данных")
    else:
        for row in rows:
            print(row)

    cur.close()
    conn.close()

paginated(3, 0)