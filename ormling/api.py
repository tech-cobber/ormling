import asyncpg
from .schema import Attribute, Model
from .crud import _create_sql, Query


class Ormling:
    """ Little home-made ORM """

    def __init__(self):
        # TODO pool
        self.connection: asyncpg.connection.Connection = None
        self.tables = []

    async def bind(self, connection_string: str = None, provider: str = None,
                   user: str = None, password: str = None,
                   host: str = None, database: str = None):
        """ Establish connection """

        if connection_string:
            self.connection = await asyncpg.connect(connection_string)
        elif user:
            if password:
                self.connection = await asyncpg.connect(
                    f"{provider}://{user}:{password}@{host}/{database}")
            else:
                self.connection = await asyncpg.connect(
                    f"{provider}://{user}@{host}/{database}")
        else:
            self.connection = await asyncpg.connect(
                f"{provider}://{host}/{database}")

    async def close(self):
        await self.connection.close()

    @property
    def Base(self):

        class Meta(type):
            def __new__(cls, name, bases, clsdict):
                clsdict['__tablename__'] = name.lower()
                if clsdict.get('__annotations__'):
                    for var, annottation in clsdict.get('__annotations__').items():
                        clsdict['__annotations__'][var] = Attribute(
                            var, annottation())
                    self.tables.append(type.__new__(cls, name, bases, clsdict))
                return type.__new__(cls, name, bases, clsdict)

        class Base(Model, metaclass=Meta):
            def __init__(self, **kwargs):
                for name, value in kwargs.items():
                    setattr(self, name, value)
        return Base

    async def create_all(self):
        for table in self.tables:
            clsdict = table.__dict__
            name = clsdict['__tablename__']
            atts = list(clsdict['__annotations__'].values())
            await self.connection.execute(_create_sql(name, atts))

    @property
    def query(self):
        return Query(self.connection)


__all__ = [
    'Ormling',
]
