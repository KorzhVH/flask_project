import sqlite3
def select_info(qry):
    conn = sqlite3.connect('vacancy_db.db')
    c = conn.cursor()
    c.execute(qry)
    result = c.fetchall()
    conn.close()
    return result


# self notes - study 12 and 13 lines
def insert_info(qry, data):
    conn = sqlite3.connect('vacancy_db.db')
    c = conn.cursor()
    c.execute(qry, data)
    conn.commit()
    conn.close()
