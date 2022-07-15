def is_called(lname):
    def func_a(name):
        print(f"Hello {name} {lname}")
    return func_a

fB = is_called("Rouz")
fB("Peiman")
