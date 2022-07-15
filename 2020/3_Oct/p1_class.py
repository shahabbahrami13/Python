class Car:
    name = "Pride"
    speed = 100
    year = 2000


c = Car()

print(c.name, c.speed)

c.speed = 120

print(c.speed)
print(Car.speed)
