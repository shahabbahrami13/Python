class House:
    def __init__(self, price):
        self.__price = 0
        self.price = price

    @property
    def price(self):           #get function
        return self.__price

    @price.setter              #set function
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Error !")
        
    def __repr__(self):
        return f"price is {self.__price}"


h = House(1000)
print(h)

h.price = -10

print(h)
