class Vector:
    def __init__(self, width, length):
        self.x = width
        self.y = length

    def __abs__(self):
        return (self.x**2+self.y**2)**0.5

    def abs2(self):
        return (self.x**2+self.y**2)**0.5

    def __str__(self):
        return f"x:{self.x} & y:{self.y}"

v = Vector(3, 4)

print(v)
print(v.abs2(), abs(v))
