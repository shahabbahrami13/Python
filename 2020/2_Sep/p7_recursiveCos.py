import math


PI = math.pi

def pow_(a, b):
    if b == 0:
        return 1
    return a*pow_(a, b-1)


def fact(n):
    if n == 1 or n == 0:
        return 1
    return n*fact(n-1)

def cos_(x, n=10):
    if n == 0:
        return x
    return ( pow_(-1, n)*pow_(x, 2*n) / fact(2*n) ) + cos_(x, n-1)

print(cos_(PI/3))
