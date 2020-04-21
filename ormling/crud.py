from .schema import Attribute
from typing import List
from asyncpg import Record


def _create_sql(name: str, attributes: List[Attribute]) -> str:
    query = f"CREATE TABLE IF NOT EXISTS {name}(\n"
    for attr in attributes[:-1:]:
        query += f"    {attr},\n"
    return query + f"    {attributes[-1]}\n)"


def _insert_sql(name: str, atts: list, values: list) -> str:
    query = f"INSERT INTO {name}({', '.join(atts)}) VALUES({', '.join(values)})"
    return query


def _select_sql(name: str, atts: list = None, where: list = None) -> str:
    if atts:
        pass
    else:
        query = f'SELECT * FROM {name}'
        if where:
            query += f" WHERE {', '.join(where)}"
        return query


def _delete_sql(*args) -> str:
    pass


class Query:

    def __init__(self, connection):
        self.connection = connection

    async def insert(self, obj):
        await self.connection.execute(_insert_sql(
            obj.__class__.__tablename__,
            list(obj.__dict__.keys()),
            [f"\'{value}\'" for value in obj.__dict__.values()]
        ))

    async def get(self, obj) -> Record:
        return await self.connection.fetch(_select_sql(
            name=obj.__class__.__tablename__,
            where=[f"{key}=\'{val}\'" for key, val in obj.__dict__.items()],
        ))

    async def all(self, obj):
        return await self.connection.fetch(_select_sql(
            name=obj.__class__.__tablename__,
        ))

    async def delete(self, obj):
        pass
