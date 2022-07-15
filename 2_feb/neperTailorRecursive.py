"""
sigma(n, i=0) x**i/i!

"""
def pow_(a, b):
    if b == 0:
        return 1
    return a*pow_(a, b-1)


def fact(n):
    if n == 1 or n == 0:
        return 1
    return n*fact(n-1)


def neper_(x, i):
    if i == 0:
        return 1
    return pow_(x, i)/fact(i) + neper_(x, i-1)


print(neper_(1, 10))
