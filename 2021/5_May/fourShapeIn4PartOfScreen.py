import turtle as t


pen = t.Pen()

def move(x, y):
    pen.up()
    pen.goto(x, y)
    pen.down()

def shape(n, size, color):
    degree = 360//n
    pen.color(color)
    for i in range(n):
        pen.fd(size)
        pen.left(degree)

xls = [150, -300, 200, -300]
yls = [150, 150, -300, -300]
nls = [3, 4, 5, 6]
szls = [80, 100, 120, 140]
crls = ['red', 'pink', 'powderblue', 'orange']

def draw(xls, yls, nls, szls,crls):
    for i in range(4):
        move(xls[i], yls[i])
        shape(nls[i], szls[i],crls[i])


draw(xls, yls, nls, szls,crls)



        
