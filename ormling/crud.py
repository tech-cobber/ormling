from .schema import Attribute
from typing import List


def _create_sql(name: str, attributes: List[Attribute]) -> str:
    query = f"CREATE TABLE IF NOT EXISTS {name}(\n"
    for attr in attributes[:-1:]:
        query += f"    {attr},\n"
    return query + f"    {attributes[-1]}\n)"


def _insert_sql(name: str, atts: list, values: list) -> str:
    query = f"INSERT INTO {name}({', '.join(atts)}) VALUES({', '.join(values)})"
    return query


def _select_sql(*args) -> str:
    pass


def _update_sql(*args) -> str:
    pass


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
