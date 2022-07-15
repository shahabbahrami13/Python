def smart_div(fun):
    def inner(a, b):
        print(f"{a}/{b}")
        if b==0:
            print("Woobs")
            return
        return fun(a, b)
    return inner

@smart_div
def divide(a, b):
    return a/b

print(divide(10, 3))
