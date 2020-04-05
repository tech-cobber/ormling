import asyncio
from ormling.api import Ormling
import datetime
import uvloop


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
DATABASE = 'postgresql://dev@localhost/mydb'
db = Ormling()


async def main():
    await db.bind(DATABASE)
    await db.connection.execute('''
        CREATE TABLE orms(
            id serial PRIMARY KEY,
            name text,
            started date
        )
    ''')
    await db.connection.execute('''
        INSERT INTO orms(name, started) VALUES($1, $2)
    ''', 'Ormling', datetime.date(2020, 4, 6))
    await db.connection.fetchrow(
        'SELECT * FROM orms WHERE name = $1', 'Ormling')
    await db.close()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
