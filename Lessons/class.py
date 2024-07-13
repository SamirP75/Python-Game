# Classes

# Form you have to fill out
class Person:
    name: str
    age: int

    def __init__(self, name: str, age:int) -> None:
        self.name = name
        self.age = age
        pass


# Once filled out you have an object

samir = Person("Samir", 11)
birat = Person("Birat", 11)

print(f'The boys name is {samir.name} and he is {samir.age} years old.')