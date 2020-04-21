import asyncio
from ormling.types import Integer, Serial, Text
from ormling.api import Ormling
from ormling.schema import primary_key
import uvloop


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
DATABASE = 'postgresql://dev@localhost/mydb'
db = Ormling()


@primary_key('id')
class Music(db.Base):
    __tablename__ = 'music'

    id: Serial
    song: Text
    artist: Text
    released: Integer


async def main():
    await db.bind(DATABASE)
    await db.create_all()
    await db.query.insert(Music(song='Welcome to My World',
                                artist='Jim Reeves',
                                released=1963))
    example_1 = await db.query.get(Music(released=1963))
    example_2 = await db.query.all(Music())
    print(f'First example: {example_1}\nSecond example: {example_2}\n')

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
