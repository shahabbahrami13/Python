num = float(input("Pls enter a number:"))

sum_ = 0

i = 0

while num>=0:
    i+=1
    sum_+=num
    num = float(input("Pls enter a number:"))

avg = sum_/i

print(f"sum= {sum_}")
print(f"average= {avg}")
