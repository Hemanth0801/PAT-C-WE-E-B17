# Operator overloading means giving extra meaning to operators (+, -, *, ==, etc.)
# for user-defined objects.
# Operator overloading allows the same operator to behave differently for different objects.




class A:
    def __init__(self,val):
        self.val = val

    def __add__(self, other):
        return self.val + other.val

obj1 = A(50)
obj2 = A(80)
print(obj1.__add__(obj2)) # obj1+obj2

