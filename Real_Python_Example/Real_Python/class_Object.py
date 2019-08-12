class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"Hello my name is {self.name}, age {self.age}")


p1 = Person("Sopha", 16)
p1.myfunc()
