import csv
import psycopg2


def update_contact(contact_id, new_first_name=None, new_phone_number=None):
    conn = psycopg2.connect(
        dbname="lab10",
        user="postgres",
        password="Nurbolatd3",
        host="localhost"
    )
    cur = conn.cursor()

    if new_first_name:
        cur.execute("""
            UPDATE Contacts
            SET first_name = %s
            WHERE contact_id = %s
        """, (new_first_name, contact_id))

    if new_phone_number:
        cur.execute("""
            UPDATE Contacts
            SET phone_number = %s
            WHERE contact_id = %s
        """, (new_phone_number, contact_id))

    conn.commit()
    cur.close()
    conn.close()


# Example usage:
update_contact(contact_id=1, new_first_name="New Name")
update_contact(contact_id=2, new_phone_number="1234567890")
