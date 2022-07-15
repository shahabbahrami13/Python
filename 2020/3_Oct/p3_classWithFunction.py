class Car:
    year = 2000
    speed = 100
    def age(self):
        return 2021 - self.year


c = Car()

print(c.speed, c.age())

c.year = 2010

print(c.speed, c.age())
