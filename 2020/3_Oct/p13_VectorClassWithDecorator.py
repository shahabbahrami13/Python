class Vector:
    def __init__(self, width, length):
        self.x = width
        self.y = length
    
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if isinstance(x, int):
            self.__x = x
        else:
            print("Error x!")

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if isinstance(self, y):
            self.__y = y
        else:
            print("Error y")


    def __abs__(self):
        return (self.x**2+self.y**2)**0.5

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"{self.x}i+{self.y}j"

    def __add__(self, w):
        return Vector(self.x+w.x, self.y+w.y)

    def addPeiman(self, w):
        return Vector(self.x+w.x, self.y+w.y)

    def __mul__(self, w):
        if isinstance(w, int):
            return Vector(self.x*w, self.y*w)
        return (self.x*w.x) + (self.y*w.y) 
        
    def __neg__(self):
        return -self.x, -self.y

    def __sub__(self, w):
##        return self + (-w)
      return self.x - w.x, self.y - w.y

    def __invert__(self):
        return self.y, self.x

    def __next__(self):
        self.x += 1
        self.y += 1
        return self
##        return self.x+1, self.y+1

    def __eq__(self, w):
        return self.x == w.x and self.y == w.y

    def __gt__(self, w):
##        return abs(self)>abs(w)
        return self.__abs__() > w.__abs__()

    def __ge__(self, w):
##        return abs(self) >= abs(w)
        return self.__abs__() >= w.__abs__()
    
            
v = Vector(3, 4)
u = Vector(-2, 7)
g = u

print(v)
print(u)
print(abs(v))
print(f"{v}+{u} = v+u")
print(v.addPeiman(u))
print(f"{v}*{u} = v*u")
print(f"{v} = {-v}")
print(f"{v}-{u} = {v-u}")
print(f"~{u} = {~u}")
print(f"next{v} = {next(v)}")
print(f"{v}*4 = {v*4}")
print(f"{g} == {u} = {g == u}")
print(f"{g} > {u} = {u > v}")
print(f"{v} >= {u} = {u >= v}")


##dir(v) to consule





