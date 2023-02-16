import sqlite3
def select_info(qry):
    conn = sqlite3.connect('vacancy_db.db')
    c = conn.cursor()
    c.execute(qry)
    result = c.fetchall()
    conn.close()
    return result

# self notes - study 12 and 13 lines
def insert_info(table_name, data):
    column = ", ".join(data.keys())
    placeholder = ':' + ', :'.join(data.keys())
    query = 'INSERT INTO %s (%s) VALUES (%s)' % (table_name, column, placeholder)
    conn = sqlite3.connect('vacancy_db.db')
    c = conn.cursor()
    c.execute(query, data)
    conn.commit()
    conn.close()
