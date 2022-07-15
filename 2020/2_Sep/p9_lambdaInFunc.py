def func(x):
    return lambda a:a*x

double = func(4)
souble = lambda a:a*4
chuble = func(4)

print(double(2))
print(souble(3))
print(chuble(4))

