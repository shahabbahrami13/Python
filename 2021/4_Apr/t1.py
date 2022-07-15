import datetime
import time
import os
import winsound
class Time:
    def __init__(self,hour=10,
                 minute=12,second=23):
        self.__hour=10
        self.__minute=12
        self.__second=23
        self.hour=hour
        self.minute=minute
        self.second=second
    @property
    def hour(self):
        return self.__hour
    @hour.setter
    def hour(self,hour):
        if isinstance(hour,int) and 0<=hour<24:
            self.__hour=hour
        
    @property
    def minute(self):
        return self.__minute
    @minute.setter
    def minute(self,minute):
        if isinstance(minute,int) and 0<=minute<60:
            self.__minute=minute
        
    @property
    def second(self):
        return self.__second
    @second.setter
    def second(self,second):
        if isinstance(second,int) and 0<=second<60:
            self.__second=second
    def isMidnight(self):
        return self.hour==0 and self.minute==0 and self.second==0
    def ding(self):
        import random
        if self.isMidnight():
            print("Ding Ding Ding")
            for i in range(10):
                winsound.Beep(500,200)
                winsound.Beep(2000,200)
                
    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"
    def __repr__(self):
        if self.hour<12:
            return f"{self.hour:02}:{self.minute:02}:{self.second:02} AM"
        elif self.hour==12:
            return f"{self.hour:02}:{self.minute:02}:{self.second:02} PM"
        else:
            return f"{self.hour%12:02}:{self.minute:02}:{self.second:02} PM"
    def __next__(self):
        self.__second=(self.__second+1)%60
        if self.__second==0:
            self.__minute=(self.__minute+1)%60
            if self.__minute==0:
                self.__hour=(self.__hour+1)%24
        self.ding()
        return self
if __name__=="__main__":
    now=datetime.datetime.now()
    t=Time(23,59,now.second)
    for i in range(60):
        print(next(t))
##        time.sleep(1)
##        os.system('cls')
