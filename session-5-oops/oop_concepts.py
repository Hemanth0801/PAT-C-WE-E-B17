#oops  logic
#class
#object
#inheritance
#encapsulation
#abstraction
#polymorphism

# inheritancem -->Inheritance OOP concept where one class gets
# (inherits) properties and methods of another class.

class Batch():
    def __init__(self, batch):
        self.batch = batch
    def publish_batch(self):
        return f"The student is from batch {self.batch}"
class student(Batch):
    def __init__(self, name,batch):
        self.name = name
        #self.batch = batch
        Batch.__init__(self, batch)
    def publish_student(self):
        return f"The student name is {self.name}"

name = student('hemu','automation')
print(name.publish_batch())
print(name.publish_student())

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





