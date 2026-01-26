#polymorphism -->the same function or method name behaves differently for different objects.
#Polymorphism = one name, many behaviors

class vehicle():
    def vehical_name(self):
        return "all have wheels"
class car(vehicle):
    def vehical_name(self):
        return "4 wheels"
class truck(vehicle):
    def vehical_name(self):
        return "5 wheels"
class bike(vehicle):
    def two_wheeler(self):
        return "2 wheels"

vehical1 = truck()
print(vehical1.vehical_name())

vehical2 = bike()
print(vehical2.vehical_name())
print(vehical2.two_wheeler())
