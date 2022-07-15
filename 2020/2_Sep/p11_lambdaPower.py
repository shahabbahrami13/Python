##or -> p = lambda a, b:1 if b==0 else a*p(a, b-1)
p = lambda a, b:1 if not b else a*p(a, b-1)

print(p(3, 4))
