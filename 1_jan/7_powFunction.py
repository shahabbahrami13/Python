def pow1(a, b):
    x = 1
    while b:
        x = x * a
        b-=1
        
    return x

print( pow1(3, 4) )

print('-'*50)

def pow2(a, b):
    x = 1
    for i in range(b):
        x*=a
    return x

print( pow2(3, 4) )
