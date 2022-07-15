

grad = ['F', 'E', 'D', 'C', 'B', 'A']
marz = ((0, 10), (10, 12), (12, 14), (14, 16), (16, 18), (18, 20))

mark = input('Pls enter a number:')
mark=mark.upper()
print(mark)


if mark in grad:
    print(marz[grad.index(mark)])
    print(f"{marz[grad.index(mark)][0]}<=score<=\
{marz[grad.index(mark)][1]}")
else:
    print("Error")
