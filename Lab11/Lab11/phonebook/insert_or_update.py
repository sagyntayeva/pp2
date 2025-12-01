from connect import connect

def insert_update(name, phone):
    conn = connect()
    if conn:
        try:
            cur = conn.cursor()
      
            cur.execute("SELECT * FROM PhoneBook WHERE first_name = %s", (name,))
            existing_entry = cur.fetchone() 
            
            if existing_entry:
           
                cur.execute("UPDATE PhoneBook SET phone = %s WHERE first_name = %s", (phone, name))
                print(f"Телефон для {name} обновлен")
            else:
               
                cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s)", (name, phone))
                print(f" {name} успешно добавлен")

            conn.commit()  

        except Exception as e:
            print(f"Произошла ошибка: {e}")
        finally:
            cur.close()
            conn.close()

insert_update("Shshs", "7478383898")
