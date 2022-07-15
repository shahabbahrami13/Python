def outer(inner):
    def fun_in():
        print("Hello")
        inner()
        print("Good Bye")
    return fun_in

@outer
def fun_a():
    print("Ahvalporsi")


fun_a()
