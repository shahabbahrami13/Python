"""
draw any shape with any angle and any color
"""
import turtle as t

def draw(n, lenth, color):
    degree = 360//n
    for i in range(n):
        pen.color(color)
        pen.fd(lenth)
        pen.left(degree)


n, length, color = int(input("تعداد ضلع:")), int(input("طول ضلع:")), input("رنگ:")
pen = t.Pen()

draw(n, length, color)
