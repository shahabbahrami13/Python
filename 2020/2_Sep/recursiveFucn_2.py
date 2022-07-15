def p(i):
    if i == 10:
        return
    print(i)
    p(i+1)

p(0)

print('-'*60)

def f(i):
    if i == 10:
        return
    f(i+1)
    print(i)

f(0)
