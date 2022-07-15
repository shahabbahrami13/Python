


if __name__=="__main__":
    c = input("Pls enter your grade:")

    chars = ["A", "B", "Error"]

    if c == chars[0]:
        print("grade between 12 and 20")
    elif c == chars[1]:
        print("grade between 0 and 20")
    else:
        print("invalid input")


