from sqlite3 import connect

def init_creature():
    conn = connect('cryptid.db')
    curs = conn.cursor()
    curs.execute('create table if not exists creature('
                 'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                 'name text unique not null, '
                 'country text not null, '
                 'area text not null, '
                 'description text not null, '
                 'aka text not null)')
    conn.commit()
    curs.close()


def init_explorer():
    conn = connect('cryptid.db')
    curs = conn.cursor()
    curs.execute('create table if not exists explorer('
                 'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                 'name text unique not null, '
                 'country text not null, '
                 'description text not null)')
    conn.commit()
    curs.close()


def init():
    init_creature()
    init_explorer()


if __name__ == '__main__':
    init()
