import matplotlib.pyplot as plt


x = list(range(-10, 11))
y = list(map(lambda a:a**2, x))


plt.plot(x, y)
plt.show()


plt.plot(x, y, '*r')
plt.show()


x1 = list(map(lambda a:a/10, x))
y = list(map(lambda a:a**2, x))
plt.plot(x, y, 'g')
plt.show()

plt.plot(x, y, '*g')
plt.show()
