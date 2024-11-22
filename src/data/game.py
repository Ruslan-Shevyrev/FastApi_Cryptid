import src.data.db_connect as db_connect


def get_word() -> str:
    query = ('select name '
             'from creature order by random() limit 1')
    conn = db_connect.get_connection()
    curs = conn.cursor()
    curs.execute(query)
    row = curs.fetchone()
    if row:
        return row[0]
    else:
        return 'test'


