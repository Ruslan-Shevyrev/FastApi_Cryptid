from src.model.Explorer import Explorer, ExplorerNoId
import src.data.db_connect as db_connect


def row_to_model(row: tuple) -> Explorer:
    id, name, country, description = row
    return Explorer(id=id,
                    name=name,
                    country=country,
                    description=description)


def model_to_dict(explorer) -> dict:
    return explorer.dict()


def get_all() -> list[Explorer]:
    query = ('select id, name, country, description '
             'from explorer')
    conn = db_connect.get_connection()
    curs = conn.cursor()
    curs.execute(query)
    return [row_to_model(row) for row in curs.fetchall()]


def get(id: int) -> Explorer:
    query = ('select id, name, country, description '
             'from explorer where id = :id')
    conn = db_connect.get_connection()
    curs = conn.cursor()
    params = {"id": id}
    curs.execute(query, params)
    return row_to_model(curs.fetchone())


def create(explorer: ExplorerNoId) -> int:
    query = ('insert into explorer(name, country, description)'
             'values (:name, :country, :description) returning id')
    params = model_to_dict(explorer)
    conn = db_connect.get_connection()
    curs = conn.cursor()
    curs.execute(query, params)
    id = curs.fetchone()[0]
    conn.commit()
    return id


def modify(explorer: Explorer) -> int:
    query = ('update explorer set name = :name, '
             ' country = :country,'
             ' description = :description '
             ' where id = :id')
    params = model_to_dict(explorer)
    conn = db_connect.get_connection()
    curs = conn.cursor()
    curs.execute(query, params)
    conn.commit()
    return explorer.id


def delete(id: int) -> bool:
    query = ('delete from explorer '
             ' where id = :id')
    params = {'id': id}
    conn = db_connect.get_connection()
    curs = conn.cursor()
    curs.execute(query, params)
    conn.commit()
    return True

