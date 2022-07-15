def multipication1(x, y):
    s = 0
    while y:
        s+=x
        y-=1
    return s

print(multipication1(11, 8))


print('-'*40)


def multipication2(x, y):
    s = 0
    for i in range(y):
        s+=x
    return s

print(multipication2(11, 8))
