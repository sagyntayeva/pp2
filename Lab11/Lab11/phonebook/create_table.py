from connect import connect

def create_table():
    command = """
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100) UNIQUE,
        phone VARCHAR(15)
    )
    """
    conn = connect()
    if conn is None:
        print("Подключение не удалось!")
        return

    print("Подключение установлено, создаем таблицу...")
    cur = conn.cursor()
    cur.execute(command)
    conn.commit()
    cur.close()
    conn.close()
    print("Таблица создана!")

create_table()
