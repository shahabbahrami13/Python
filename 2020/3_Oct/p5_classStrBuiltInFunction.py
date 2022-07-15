class Car:
    def __init__(self):
        self.year = 2000
        self.speed = 100

    def __str__(self):
        return f"speed = {self.speed}, age = {self.age()}"
        
    def age(self):
        return 2021 - self.year


c = Car()

print(c.speed, c.speed, c.age())

c.year = 2010

print(c.speed, c.speed, c.age())

print(c)
