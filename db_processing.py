import sqlite3
vacancy_data = {
            "vacancy_id": 1,
            "creation_date": "",
            "position_name": "",
            "company": "",
            "description": "",
            "contacts_id": "",
            "comment": "",
            "user_id": 1
        }

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


def get_vacancy_by_id(vac_id):
    conn = sqlite3.connect('vacancy_db.db')
    c = conn.cursor()
    query = "Select * from vacancy where id='%s'" % (vac_id)
    result = c.execute(query)
    conn.close()
    return result
