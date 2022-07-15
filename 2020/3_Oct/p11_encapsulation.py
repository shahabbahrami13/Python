class T:
    def __init__(self):
        self.a = 10
        self._b = 20
        self.__c = 30

    def __str__(self):
        return f"a = {self.a}\n_b = {self._b}\n__c = {self.__c}"


t = T()
print(t)
print(t.a)
print(t._b)
print(t._T__c)

t._T__c = 21234

print(t._T__c)
