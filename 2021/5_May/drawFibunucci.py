import turtle as t


pen = t.Pen()

pen.speed(0)

def fib(n):
    f=[1, 1]
    for i in range(2, n+1):
        f.append(sum(f[-2:]))
    return f

##print(fib(30))

pen.color('pink')

def spiralFib(n):
    for i in fib(n):
        pen.circle(i, 90)


spiralFib(10)
