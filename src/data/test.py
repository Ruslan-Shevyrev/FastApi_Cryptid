from sqlite3 import connect

query = ('select id, name, country, area, description, aka '
         'from creature')
conn = connect('cryptid.db')
curs = conn.cursor()
curs.execute(query)
for row in curs.fetchall():
    print(row)