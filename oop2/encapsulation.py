class Dog:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__id = "3213"

    def get_id(self):
        return self.__id

    def set_id(self, id: str):
        if len(id) == 4:
            self.__id = id
        raise Exception("Cannot raise id if its not 4 characters")

d = Dog("Ales")
print(d.get_id())
print("konec")



