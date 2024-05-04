import csv
import psycopg2

def enter_from_console():
    conn = psycopg2.connect(
        dbname="lab10",
        user="postgres",
        password="Nurbolatd3",
        host="localhost"
    )
    cur = conn.cursor()

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email (optional): ")
    address = input("Enter address (optional): ")

    cur.execute("""
        INSERT INTO Contacts (first_name, last_name, phone_number, email, address)
        VALUES (%s, %s, %s, %s, %s)
    """, (first_name, last_name, phone_number, email, address))

    conn.commit()
    cur.close()
    conn.close()


# Example usage:
enter_from_console()
