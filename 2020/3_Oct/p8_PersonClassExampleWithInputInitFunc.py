import datetime


class Person:
    def __init__(self, firstname, lastname, y=2010):
        self.fname = firstname
        self.lname = lastname
        self.year = y

    def age(self):
        return datetime.datetime.now().year - self.year

    def __str__(self):
        return f"His name is {self.fname} {self.lname} and he is {self.age()} \
years old."
    

p = Person('Reza', 'Sadeghi', 2000)

print(p)
