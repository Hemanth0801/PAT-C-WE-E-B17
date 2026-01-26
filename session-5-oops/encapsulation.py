# encapsulation is a oops concept that allows biding od data in a class and control the obj accessibility

class A:
    def __init__(self):
        self._a =10  #protected obj / declare with '_'
        self.__b =20 #private / declare with'__'
        self.c =30   #public  /declare with no underscore
    def get_value(self):
        return self.__b
    def set_value01(self):
        return self._a
class B(A):
    def get_value(self):
        return self.__b
obj = A()
# boj2 = B()
print(obj.set_value01())
# print(boj2.get_value())
