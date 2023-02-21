import sqlite3
class DB:
    def __enter__(self):
        self.conn = sqlite3.connect('vacancy_db.db')
        self.c = self.conn.cursor()
        return self

    def query(self, qry):
        self.c.execute(qry)
        result = self.c.fetchall()
        return result

    def insert(self, qry, data):
        self.c.execute(qry, data)
        self.conn.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.c.close()
        self.conn.close()
