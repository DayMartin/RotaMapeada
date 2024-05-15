from db.database import get_mysql_connection

conn = get_mysql_connection()

class Person:
    def create(self, username, password):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO people (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        cursor.close()

    def __repr__(self):
        return f"Person(id={self.id}, name={self.name})"
