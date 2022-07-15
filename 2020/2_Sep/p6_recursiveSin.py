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

def sin_(x, i=10):
    if i == 0:
        return x
    return pow_(-1, i)*pow_(x, 2*i+1) / fact(2*i+1)+sin_(x, i-1)

print(sin_(PI/2))
