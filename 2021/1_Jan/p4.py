a = input("Enter a number for trangle:")
b = input("Enter a number for trangle:")
c = input("Enter a number for trangle:")


if a+b>c and a+c>b and b+c>a:
    print("mosalas")
    if a==b==c:
        print("motasavi azla")
    elif a==b or a==c or b==c:
        print("motasavi saghein")
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("mosalase ghaemo zavie")
else:
    print("mosalas nist")



##if a+b<=c:
##    print("invalid input")
##elif a+c<=b:
##    print("invalid input")
##elif b+c<=a:
##    print("invalid input")
