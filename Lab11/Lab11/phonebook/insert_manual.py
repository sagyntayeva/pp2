from connect import connect

def insert_manual():
    first_name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s)", 
    (first_name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Данные успешно добавлены!")

insert_manual()

