def outer(inner):
    def fun_in():
        print("Hello")
        inner()
        print("Good Bye")
    return fun_in

def fun_a():
    print("Ahvalporsi")


##fun_a()

fun_a = outer(fun_a)
fun_a()
