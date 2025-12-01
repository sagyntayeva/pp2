from connect import connect

def delete_data():
    value = input("Введите имя или номер телефона для удаления: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM PhoneBook
        WHERE first_name = %s OR phone = %s
    """, (value, value))

    if cur.rowcount == 0:
        print(f"Контакт не найден")
    else:
        print("Контакт удалён")

    conn.commit()
    cur.close()
    conn.close()

delete_data()

