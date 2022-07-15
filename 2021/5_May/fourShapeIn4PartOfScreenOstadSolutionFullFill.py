import turtle as t


pen = t.Pen()

def move(x, y):
    pen.up()
    pen.goto(x, y)
    pen.down()

def shape(n, size, color):
    degree = 360//n
    pen.color(color)
    pen.begin_fill()
    for i in range(n):
        pen.fd(size)
        pen.left(degree)
    pen.end_fill()

param = {'xls':[150, -300, 200, -300],
         'yls':[150, 150, -300, -300],
         'nls':[3, 7, 4, 5],
         'szls':[150, 60, 120, 100],
         'crls':['red', 'pink', 'powderblue', 'orange']}

def draw(param):
    for i in range(4):
        move(param['xls'][i], param['yls'][i])
        shape(param['nls'][i], param['szls'][i],param['crls'][i])


draw(param)



        
