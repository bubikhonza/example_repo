from dataclasses import dataclass

@dataclass
class Cat:
    age: int
    race: str
    name: str
    home: str

    def meow(self):
        print("meow")

class Cat:
    def __init__(self, age: int, race: str, name: str, home: str):
        self.age = age
        self.race = race
        self.name = name
        self.home = home

    def meow(self):
        print("meow")

