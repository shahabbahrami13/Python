import turtle as t
import random


pen = t.Pen()
pen.speed(0)

def move(x, y):
    pen.up()
    pen.goto(x, y)
    pen.down()

def shape(n, size):
    degree = 360/n
    for i in range(n):
        pen.fd(size)
        pen.left(degree)

def tree(n, size, x, Ltree, Wtree):
        move(random.randrange(-x, x), random.randrange(-x, x))
        sz = random.randrange(Ltree, Wtree) #هرچي دور تر تيره تر هرچي نزديکتر سبز روشنتر
        l = Wtree-Ltree
        pen.color(0, (sz-Ltree)/l, 0)
        pen.begin_fill()
        shape(n, sz)
        pen.end_fill()

def jungle(n, size, x, Ltree, Wtree, num):
    for i in range(num):
        tree(n, size, x, Ltree, Wtree)

jungle(3, 100, 300, 20, 60, 100)
