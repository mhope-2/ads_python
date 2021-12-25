class Animal:
    def __init__(self) -> None:
        print("Animal Created")
    
    def move(self):
        print("Animal moving")

    def cry(self):
        print("Animal crying")


class Dog(Animal):
    def __init__(self) -> None:
        print("Dog created")
    
    def move(self):
        print("Dog moving")


dog = Animal()
dog.__name