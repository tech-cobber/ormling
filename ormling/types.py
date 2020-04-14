class Type:
    __slots__ = 'oid', 'name', 'kind', 'schema'

    def __init__(self, name: str, kind=None, schema=None, oid=None):
        self.name = name
        self.kind = kind
        self.schema = schema
        self.oid = oid

    def __str__(self):
        return self.name


class Serial(Type):
    def __init__(self):
        super().__init__(name='serial')


class Integer(Type):
    def __init__(self):
        super().__init__(name='integer')


class Float(Type):
    def __init__(self):
        super().__init__(name='float')


class Text(Type):
    def __init__(self):
        super().__init__(name='text')
