class Taghvim:
    months = (0, 31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29)
    monthsName = ('فروردين', 'ارديبهشت', 'خرداد', 'تير', 'مرداد', 'شهريور', 'مهر', 'آبان', 'آذر', 'دي', 'بهمن', 'اسفند')
    def __init__(self, d, m ,y):
        self.__day = 1
        self.__month = 1
        self.__year = 1
        self.day = d
        self.month = m
        self.year = y

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, y):
        if isinstance(y, int) and y>0:
            self.__year = y
        else:
            print("Year Error!")

    @property
    def month(self):
        return self.__month
    @month.setter
    def month(self, m):
        if isinstance(m, int) and 0<m<13:
            self.__month = m
        else:
            print("Month Error!")

    @property
    def day(self):
        return self.__day
    @day.setter
    def day(self, d):
        if isinstance(d, int) and 0<d<=self.months[self.month]:
            self.__day = d
        else:
            print("Day Error!")

    def __next__(self):
        self.__day += 1
        if self.__day > self.months[self.__month]:
            self.__day = 1
            self.__month += 1
        if self.month>12:
            self.month = 1
            self.__year += 1
        return self

    def __str__(self):
        return f"{self.year}/{self.month:02}/{self.day:02}"

    def __repr__(self):
        return f"{self.day}/{self.monthsName[self.month-1]}/{self.year}"


if __name__ == "__main__":
    dt = Taghvim(22, 12, 1399)
    for i in range(365):
        print( next(dt) )


            
