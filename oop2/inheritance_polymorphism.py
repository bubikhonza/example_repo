from typing import Callable


class Dog:
    def __init__(self, age: int):
        self.age = age

    def run(self):
        print("I am running")

    def _wag_tail(self):
        print(self.age)
        print("I am happy")

    def bark(self):
        self._wag_tail()
        print("I am barking")

class Retriever(Dog):
    pass

class Buldocek(Dog):
    def __init__(self, age: int, special_treat: str):
        super().__init__(age)
        self.special_treat = special_treat

    def bark(self):
        self._wag_tail()
        print("chrochro")

    def run(self):
        print(f"i am running big distance")


r = Retriever(age=5)
b = Buldocek(age=3, special_treat="snack bar")


animal_list: list[Dog] = [r, b]
for animal in animal_list:
    animal.bark()



class Animal:
    def __init__(self, speak_behaviour: Callable):
        self.speak_behaviour = speak_behaviour

    def speak(self):
        self.speak_behaviour()

def woof():
    print("woof")

def no_sound():
    print("nothing")

def booing():
    print("booing")

dog = Animal(speak_behaviour=woof)
cow = Animal(speak_behaviour=booing)
dog.speak()
cow.speak()

class DogFileUtils:
    def save_dog(self, dog: Dog):
        pass
    def read_dog(self, dog_id: int):
        pass

