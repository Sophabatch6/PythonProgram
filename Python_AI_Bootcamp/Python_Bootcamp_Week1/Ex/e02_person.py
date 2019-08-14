class Person:
    name = ""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def introduce(self):
        print(f"Hi, My name is {self.name} .")


somebody = Person("Kevin")

somebody.get_name()
somebody.introduce()
