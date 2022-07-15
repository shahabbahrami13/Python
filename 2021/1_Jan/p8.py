x = int(input("Enter a num:"))

x1 = 1
x2 = 2
i = 1
y = 0

while y<x:
    x1 = x2
    x2 = y
    y = x1+x2
    i += 1 

print(i)

