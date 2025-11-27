from connect import connect

def update_data():
    old_name = input("Имя пользователя для обновления: ")
    new_name = input("Новое имя: ")
    new_phone = input("Новый телефон: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        UPDATE PhoneBook
        SET first_name = %s, phone = %s
        WHERE first_name = %s
    """, (new_name, new_phone, old_name))

    if cur.rowcount == 0:
        print("Пользователь не найден.")
    else:
        print("Данные обновлены.")

    conn.commit()
    cur.close()
    conn.close()

update_data()

