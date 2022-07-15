n = int(input("Pls enter n:"))

def printStar1(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end='')
        print()

def printStar2(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end='')
        print()


printStar1(n)
printStar2(n)


def mountain(x=10):
    for i in range(1, x+1):
        printStar1(i)
        printStar2(i)
        print()

print("Alborz mountain:")

mountain(n)
