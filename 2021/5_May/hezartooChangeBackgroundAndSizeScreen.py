import turtle as t


def hezartoo(n, size, color):
    degree = 360//n
    pen.color(color)
    for i in range(size):
        pen.fd(i)
        pen.left(degree)

n = int(input("Pls enter number of side:"))

size = int(input("Pls enter side length:"))

color = input("Enter color of hezartoo:")

pen = t.Pen()

pen.speed(0)

t.bgcolor('red')

##t.screensize(800, 600, 'pink')

hezartoo(n, size, color)
