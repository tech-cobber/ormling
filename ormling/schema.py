from .types import Type


class Attribute:
    __slots__ = 'name', 'type'

    def __init__(self, name_: str, type_: Type):
        self.name = name_
        self.type = type_

    def __str__(self):
        return f'{self.name} {str(self.type)}'


class Key:
    def __init__(self, attribute: Attribute, kind: str) -> None:
        self.attribute = attribute
        self.kind = kind

    def __str__(self):
        return f'{self.attribute} {self.kind}'


def primary_key(name):
    def decorator(cls):
        attr: Attribute = cls.__annotations__[name]
        cls.__annotations__[name] = Key(attr, 'PRIMARY KEY')
        return cls
    return decorator
