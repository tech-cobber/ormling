# Ormling

Ormling is a small home-made ORM, build on top of the asyncpg.

### Features!
Ormling uses python's native declarative mechanism - annotations to declare tables
```python
@primary_key('id')
class Music(db.Base):
    __tablename__ = 'music'

    id: Serial
    song: Text
    artist: Text
    released: Integer
```

### Usage
See no reason to publish it to PyPI, so...
```sh
$ pip3 install dist/ormling-0.1.0-py3-none-any.whl
```
... and then
```python
import ormling
```

### Examples
And I got some [examples](https://github.com/tech-cobber/ormling/tree/master/examples)

### TODO
Basically everything, but currenly you can take a look at this project -> [TODO](https://github.com/tech-cobber/ormling/projects/1)