import turtle as t


pen = t.Pen()

pen.color(.5, .5, 1)

pen.shape('turtle')

for i in range(100):
    pen.fd(i)
    pen.left(90)

pen.shape('arrow')

pen.fd(100)

pen.left(90)

pen.color(0.5, 0, 0)

pen.pensize(10)

pen.fd(100)

pen.shapesize(10)


