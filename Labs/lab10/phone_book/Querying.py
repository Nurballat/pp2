import csv
import psycopg2

def query_contacts_by_name(first_name):
    conn = psycopg2.connect(
        dbname="lab10",
        user="postgres",
        password="Nurbolatd3",
        host="localhost"
    )
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM Contacts
        WHERE first_name = %s
    """, (first_name,))

    contacts = cur.fetchall()

    cur.close()
    conn.close()

    return contacts


# Example usage:
result = query_contacts_by_name("John")
print(result)
