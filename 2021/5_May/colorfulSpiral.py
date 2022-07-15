import turtle as t


pen = t.Pen()

pen.speed(0)

t.bgcolor(.2, .2, .2)

def spiral(n, size):
    degree = 360//n
    for i in range(size):
        c = i/size
##        pen.color(c, 1-c, c)
        pen.color(1, 1-c, 1)
        pen.fd(i)
        pen.left(90)

n, size = 4, 300

spiral(n, size)
