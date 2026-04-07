class Bar:
    COUNTER = 0
    def __init__(self, x):
        self.x = x
        Bar.add_counter()

    @classmethod
    def add_counter(cls):
        cls.COUNTER += 1

    @staticmethod
    def add_counter2():
        Bar.COUNTER += 1

    @classmethod
    def get_number_of_created_instances(cls):
        return cls.COUNTER

x = Bar(6)
y = Bar(7)
print(Bar.get_number_of_created_instances())
c = Bar(10)
print(Bar.get_number_of_created_instances())


class Car:
    def __init__(self):
        self.engine = Engine()

class Car2:
    def __init__(self, engine: Engine):
        self.engine = engine

class Engine:
    ...

e = Engine()
c = Car2(
    engine=e
)
