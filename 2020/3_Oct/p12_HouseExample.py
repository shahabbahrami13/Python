class House:
    def __init__(self, price):
        self.price = price
    def __repr__(self):
        return f"price is {self.price}"

h = House(1000)
print(h)

h.price = -10

print(h)
