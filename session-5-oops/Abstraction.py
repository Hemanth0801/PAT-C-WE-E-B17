# Abstraction is a oops concept that allows hiding the key functionality from outside call

from abc import ABC, abstractmethod #import  ABC class to use abstarction
class A(ABC):
    @abstractmethod
    def Addition(self):
        pass
class B(A):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def Addition(self):
        total = self.a + self.b
        return(total)
obj = B(10,20)
print(obj.Addition())



