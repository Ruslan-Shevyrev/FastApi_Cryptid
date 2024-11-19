from src.model.User import User, UserNoId
import src.data.db_connect as db_connect


def row_to_model(row: tuple) -> User:
    id, name, password = row
    return User(id=id,
                name=name,
                password=password)


def model_to_dict(creature) -> dict:
    return creature.dict()


def get_all() -> list[User]:
    query = ('select *'
             'from user')
    conn = db_connect.get_connection()
    curs = conn.cursor()
    curs.execute(query)
    return [row_to_model(row) for row in curs.fetchall()]


def get(id: int) -> User:
    query = ('select *'
             'from user where id = :id')
    conn = db_connect.get_connection()
    curs = conn.cursor()
    params = {"id": id}
    curs.execute(query, params)
    return row_to_model(curs.fetchone())


def get_by_username(username: str) -> User:
    query = ('select *'
             'from user where name = :username')
    conn = db_connect.get_connection()
    curs = conn.cursor()
    params = {"username": username}
    curs.execute(query, params)
    return row_to_model(curs.fetchone())


def create(user: UserNoId) -> int:
    query = ('insert into user(name, password)'
             'values (:name, :password) returning id')
    params = model_to_dict(user)
    conn = db_connect.get_connection()
    curs = conn.cursor()
    curs.execute(query, params)
    id = curs.fetchone()[0]
    conn.commit()
    return id


def modify(user: User) -> int:
    query = ('update user set user = :name, '
             ' password = :password '
             ' where id = :id')
    params = model_to_dict(user)
    conn = db_connect.get_connection()
    curs = conn.cursor()
    curs.execute(query, params)
    conn.commit()
    return user.id


def delete(id: int) -> bool:
    query = ('delete from user '
             ' where id = :id')
    params = {'id': id}
    conn = db_connect.get_connection()
    curs = conn.cursor()
    curs.execute(query, params)
    conn.commit()
    return True