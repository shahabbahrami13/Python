import math


PI = math.pi

r = float(input("Pls enter radius:"))
s = (r**2)*PI

print(f"radius={r} va pi={PI} va area={s}")

print("r=%d va s=%8.2f va pi=%f"%(r,s,PI))
print("r=%d va s=%08.2f va pi=%f"%(r,s,PI))
print("r=%d va s=%06.4f va pi=%06.5f"%(r,s,PI))
print("r=%d va s=%06.10f va pi=%06.2f"%(r,s,PI))

print("r={} va s={} va PI={}".format(r, s, PI))
print("r={0} va s={2} va PI={1}".format(r, s, PI))

print("r={} va s={:06.2} va PI={:6.2}".format(r, s, PI))
print("r={} va s={:06.10} va PI={:6.10}".format(r, s, PI))
print("r={} va s={:5.2} va PI={:.3}".format(r, s, PI))

print("*"*10)

print(f"r={r} va s={s:.2} PI={PI:.2}")
print(f"r={r} va s={s:.4} PI={PI:.4}")
print(f"r={r} va s={s:.4f} PI={PI:.4f}")
print(f"r={r} va s={s:.2f} PI={PI:.2f}")


print("@"*20)

m = 15
n = 10

print(f"x={m:x} va y={n:x}")
print(f"x={m:o} va y={n:o}")

