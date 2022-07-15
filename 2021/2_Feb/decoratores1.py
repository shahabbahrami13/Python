def inc(x):
    return x+1
def dec(x):
    return x-1

def exe(f, a):
    return f(a)

s=10
print(exe(inc, s))
print(exe(dec, s))

func = exe

print(func(inc, s))
print(func(dec, s))
