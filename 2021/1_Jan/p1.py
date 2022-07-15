"""
18<=grade<=20  A
12<=grade<=18  B
0<=grade<=12   C
grade<=0 or grade>=20 Error

"""
if __name__=="__main__":
    
    grade = float(input("Pls enter a your grade:"))

    if 18<=grade and grade<=20:
        print("A")
    elif 12<=grade<=18:
        print("B") 
    elif 0<=grade<=12:
        print("C")
    else:
        print("Error")
