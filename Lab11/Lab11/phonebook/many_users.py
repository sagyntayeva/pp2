
from connect import connect

def many(info):
    conn = connect()
    cur = conn.cursor()
    for name, phone in info:
            cur.execute("SELECT * FROM PhoneBook WHERE first_name = %s", (name,))
            existing_entry = cur.fetchone() 
            
            if existing_entry:
           
                cur.execute("UPDATE PhoneBook SET phone = %s WHERE first_name = %s", (phone, name))
                print(f"Телефон для {name} обновлен")
            else:
               
                cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s)", (name, phone))
                print(f" {name} успешно добавлен")

             
    conn.commit()
    cur.close()
    conn.close()

many([('Aliya', '87771234567'), ('Zhanel', '6766987698')])



