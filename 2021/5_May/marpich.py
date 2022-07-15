import turtle as t

pen = t.Pen()

pen.speed(0)


def shape(n, size, color):
    pen.color(color)
    degree = 360//n
    for i in range(n):
        pen.fd(size)
        pen.left(degree)


def marpich(n, size, color):
    for i in range(10, size, 10):
        shape(n, i, color)

marpich(17, 400, 'silver')

