from sqlite3 import connect

query = ('select id '
         'from user')
conn = connect('../../../src/data/cryptid.db')
curs = conn.cursor()
curs.execute(query)
for row in curs.fetchall():
    print(row)