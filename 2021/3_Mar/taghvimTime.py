from taghvim import Taghvim
from time_complete import Time


class TaghvimTime(Time, Taghvim):
    def __init__(self, day=10, month=10, year=1399, hour=33, minute=22, second=23):
        Taghvim.__init__(self, day, month, year)
        Time.__init__(self, hour, minute, second)

    def __str__(self):
        return Taghvim.__str__(self)+"  "+Time.__str__(self)

    def __next__(self):
        Time.__next__(self)
        if Time.isMidnight(self):
            Taghvim.__next__(self)
        return self    

if __name__ == "__main__":
    tt = TaghvimTime(hour = 23, minute = 59, second = 50)
    for i in range(20):
        print(next(tt))
