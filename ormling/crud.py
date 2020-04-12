from .schema import Attribute
from typing import List
# TODO classes?


def create_sql(name: str, attributes: List[Attribute]):
    query = f"CREATE TABLE {name}(\n"
    for attr in attributes[:-1:]:
        query += f"    {attr},\n"
    return query + f"    {attributes[-1]}\n)"


def select_sql(*args):
    pass


def update_sql(*args):
    pass


def delete_sql(*args):
    pass
