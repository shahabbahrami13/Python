import turtle as t


t.speed(-10)

def sun():
    t.color('red', 'yellow')
    t.begin_fill()
    count = 0
    while True:
        count += 1
        t.forward(200)
        t.left(92)
        if abs(t.pos())<1 or count>100:
            break
    t.end_fill()


sun()
