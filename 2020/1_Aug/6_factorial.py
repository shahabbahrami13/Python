n = int(input("Pls enter n:"))

def fact(n):
    x = 1
    for i in range(n):
        x += x*i
    return x


print(fact(n))
