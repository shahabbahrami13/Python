"""
e^(x, n) = sigma(i=0, n) x^i / i!

"""
import math

def pow_(a, b):
    p = 1
    for i in range(b):
        p*=a
    return p

def fact(n):
    p = 1
    for i in range(n):
        p += p*i
    return p

def neper(x=1, n=10):
    s = 0
    for i in range(0, n+1):
        s += pow_(x, i) / fact(i)
    return s

print(neper(1, 40))
print(neper())

print('^'*60)

print(math.e)
print(math.exp(1))
