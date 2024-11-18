from src.model.Creature import Creature, CreatureNoId
import src.data.db_connect as db_connect


def row_to_model(row: tuple) -> Creature:
    id, name, country, area, description, aka = row
    return Creature(id=id,
                    name=name,
                    country=country,
                    area=area,
                    description=description,
                    aka=aka)


def model_to_dict(creature) -> dict:
    return creature.dict()


def get_all() -> list[Creature]:
    query = ('select id, name, country, area, description, aka '
             'from creature')
    conn = db_connect.get_connection()
    curs = conn.cursor()
    curs.execute(query)
    return [row_to_model(row) for row in curs.fetchall()]


def get(id: int) -> Creature:
    query = ('select id, name, country, area, description, aka '
             'from creature where id = :id')
    conn = db_connect.get_connection()
    curs = conn.cursor()
    params = {"id": id}
    curs.execute(query, params)
    return row_to_model(curs.fetchone())


def create(creature: CreatureNoId) -> int:
    query = ('insert into creature(name, country, area, description, aka)'
             'values (:name, :country, :area, :description, :aka) returning id')
    params = model_to_dict(creature)
    conn = db_connect.get_connection()
    curs = conn.cursor()
    curs.execute(query, params)
    id = curs.fetchone()[0]
    conn.commit()
    return id


def modify(creature: Creature) -> int:
    query = ('update creature set name = :name, '
             ' country = :country,'
             ' area = :area,'
             ' description = :description, '
             ' aka = :aka'
             ' where id = :id')
    params = model_to_dict(creature)
    conn = db_connect.get_connection()
    curs = conn.cursor()
    curs.execute(query, params)
    conn.commit()
    return creature.id


def delete(id: int) -> bool:
    query = ('delete from creature '
             ' where id = :id')
    params = {'id': id}
    conn = db_connect.get_connection()
    curs = conn.cursor()
    curs.execute(query, params)
    conn.commit()
    return True