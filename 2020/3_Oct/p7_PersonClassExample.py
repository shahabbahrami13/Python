class Person:
    def __init__(self):
        self.fname = 'Peiman'
        self.lname = 'Rouz'
        self.birthday = 1989

    def age(self):
        return 2021-self.birthday


p = Person()

print(p.fname, p.lname, p.age())
