import csv
from connect import connect

def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) < 2:
                print(f"Пропущена строка: {row}")
                continue
            cur.execute(
                "INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    cur.close()
    conn.close()

insert_from_csv('contacts.csv')
