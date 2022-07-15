def pow_(a, b):
    if b == 0:
        return 1
    return a*pow_(a, b-1)

print(pow_(3, 4))
