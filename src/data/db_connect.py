from sqlite3 import connect, Connection


class SQLite:
    conn: Connection
    db_name: str

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conn = connect(db_name, check_same_thread=False)

    def get_connection(self) -> Connection:
        if not self.conn:
            self.conn = connect(self.db_name, check_same_thread=False)
        return self.conn


sqlite: SQLite


def init():
    global sqlite
    sqlite = SQLite('data/cryptid.db')


def get_connection() -> Connection:
    return sqlite.get_connection()


init()
