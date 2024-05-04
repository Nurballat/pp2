import csv
import psycopg2

def upload_from_csv(file_path):
    conn = psycopg2.connect(
        dbname="lab10",
        user="postgres",
        password="Nurbolatd3",
        host="localhost"
    )
    cur = conn.cursor()

    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # Skip header
        for row in reader:
            first_name, last_name, phone_number, email, address = row
            cur.execute("""
                   INSERT INTO Contacts (first_name, last_name, phone_number, email, address)
                   VALUES (%s, %s, %s, %s, %s)
               """, (first_name, last_name, phone_number, email, address))

    conn.commit()
    cur.close()
    conn.close()

# Example usage:
upload_from_csv('data.csv')

