n, m = int(input("Pls enter n:")), int(input("Pls enter m:"))

def resualt(x, y):
    x += 1
    return x, y+1

def squar(x, y):
    y = y**2
    return x**2, y

def cube(x, y):
    y = pow(y, 3)
    return x*x*x, y

def absolut(x, y):
    if x<0:
        x = -x 
    return x, abs(y)



print(resualt(n, m))

print('*'*50)

print(squar(n, m))

print('*'*50)

print(cube(n, m))

print('*'*50)

print(absolut(n, m))
print()
