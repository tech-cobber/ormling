import asyncpg


class Ormling:
    """ Little home-made ORM """

    def __init__(self):
        self.connection: asyncpg.connection.Connection = None

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
