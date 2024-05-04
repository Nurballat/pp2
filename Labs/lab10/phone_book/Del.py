import psycopg2


def delete_contact_by_username(username):
    conn = psycopg2.connect(
        dbname="lab10",
        user="postgres",
        password="Nurbolatd3",
        host="localhost"
    )
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM Contacts
        WHERE first_name = %s
    """, (username,))

    conn.commit()
    cur.close()
    conn.close()


# Example usage:
delete_contact_by_username("John")
