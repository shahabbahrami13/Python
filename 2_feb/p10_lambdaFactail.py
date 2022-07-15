##or - >  h = lambda n:1 if not n else n*h(n-1)
h = lambda n:1 if n==0 else n*h(n-1)

print(h(5))
