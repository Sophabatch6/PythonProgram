class Person:
    def get_info(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        print(f"Hello, My name is {self.first_name} {self.last_name}, I am a Person!!")


class Student(Person):
    def introduce(self):
        print(f"Hello, My name is {self.first_name} {self.last_name}, I am a Student!!")


class Teacher(Person):
    def introduce(self):
        print(f"Hello, My name is {self.first_name} {self.last_name}, I am a Teacher!!")


P = Person()
S = Student()
T = Teacher()
P.get_info("ENG", "SOPHA")
P.introduce()
S.get_info("NOUP", "SOVAN")
S.introduce()
T.get_info("KEVIN", "SABBE")
T.introduce()
