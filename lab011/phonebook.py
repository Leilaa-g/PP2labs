import psycopg2
import csv
from tabulate import tabulate
import re

# PostgreSQL деректер базасына қосылу
conn = psycopg2.connect(host="localhost", dbname="lab10", user="postgres",
                        password="Almaty250505", port=5432)

cur = conn.cursor()

# Кестені жасау (егер ол жоқ болса)
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL, 
    phone VARCHAR(255) NOT NULL
)
""")

def is_valid_phone(phone):
    # Телефон нөмірінің дұрыстығын тексеру (формат: +1234567890 немесе 1234567890)
    if re.match(r"^\+?\d{10,15}$", phone):
        return True
    else:
        return False

def insert_data():
    print('Type "csv" or "con" to choose option between uploading csv file or typing from console: ')
    method = input().lower()
    if method == "con":
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")
        if not is_valid_phone(phone):
            print("Қате: Телефон нөмірі дұрыс емес.")
            return
        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
    elif method == "csv":
        filepath = input("Enter a file path with proper extension: ")
        try:
            with open(filepath, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip the header row
                for row in reader:
                    name, surname, phone = row
                    if not is_valid_phone(phone):
                        print(f"Қате: {name} {surname} үшін телефон нөмірі дұрыс емес: {phone}")
                    else:
                        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
        except FileNotFoundError:
            print("Қате: Файл табылмады.")
        except Exception as e:
            print(f"Қате: {e}")

def display_data():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    if rows:
        print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))
    else:
        print("No data found in the database.")

def display_csv_data():
    file_path = input("Enter the CSV file path: ")
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            if rows:
                print(tabulate(rows, headers=["Name", "Surname", "Phone"]))
            else:
                print("No data found in the CSV file.")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"Error: {e}")

def search_by_pattern():
    pattern = input("Enter the pattern to search (part of name, surname, or phone): ")
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR surname ILIKE %s OR phone ILIKE %s", 
                (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
    rows = cur.fetchall()
    if rows:
        print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))
    else:
        print("No matching records found.")

def insert_or_update_user():
    name = input("Enter Name: ")
    surname = input("Enter Surname: ")
    phone = input("Enter Phone: ")
    
    cur.execute("SELECT * FROM phonebook WHERE name = %s AND surname = %s", (name, surname))
    user = cur.fetchone()
    
    if user:
        print("User exists, updating phone number...")
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s AND surname = %s", (phone, name, surname))
    else:
        print("New user, adding to the phonebook...")
        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
    
    conn.commit()

def delete_by_username_or_phone():
    identifier = input("Enter the username or phone number to delete: ")
    
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (identifier, identifier))
    conn.commit()

def insert_multiple_users(users_list):
    # Параметр ретінде берілген users_list - бұл тізім, әр элемент - (name, surname, phone) түрінде
    for user_data in users_list:
        name, surname, phone = user_data
        
        # Телефон нөмірін тексеру
        if not is_valid_phone(phone):
            print(f"Invalid phone number for {name} {surname}: {phone}")
            continue
        
        # Қолданушы бар ма тексеру
        cur.execute("SELECT * FROM phonebook WHERE name = %s AND surname = %s", (name, surname))
        user = cur.fetchone()
        
        if user:
            print(f"User {name} {surname} exists, updating phone number...")
            cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s AND surname = %s", (phone, name, surname))
        else:
            print(f"Adding new user: {name} {surname}")
            cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))

    conn.commit()

def query_data_with_pagination(limit, offset):
    cur.execute("SELECT * FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    if rows:
        print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))
    else:
        print("No more data.")

# Тест ретінде бірнеше қолданушыны қосу
users = [
    ("John", "Doe", "1234567890"),
    ("Jane", "Smith", "+12345678901"),
    ("Alice", "Johnson", "9876543210")
]
insert_multiple_users(users)

# Беттеу тесті
query_data_with_pagination(2, 0)

while True:
    print("""
    List of the commands:
    1. Type "i" or "I" to INSERT data to the table.
    2. Type "u" or "U" to UPDATE data in the table.
    3. Type "q" or "Q" to QUERY data in the table.
    4. Type "d" or "D" to DELETE data from the table.
    5. Type "s" or "S" to SEE the values in the table or CSV file.
    6. Type "f" or "F" to close the program.
    """)
    command = input().lower()

    if command == "i":
        insert_data()
    elif command == "u":
        insert_or_update_user()
    elif command == "d":
        delete_by_username_or_phone()
    elif command == "q":
        search_by_pattern()
    elif command == "s":
        choice = input('Do you want to see data from the (1) database or (2) CSV file? Enter 1 or 2: ')
        if choice == "1":
            display_data()
        elif choice == "2":
            display_csv_data()
    elif command == "f":
        break

conn.commit()
cur.close()
conn.close()
