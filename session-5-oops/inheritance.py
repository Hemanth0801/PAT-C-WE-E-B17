# inheritancem -->Inheritance OOP concept where one class gets
# (inherits) properties and methods of another class.

# class Batch():
#     def __init__(self, batch):
#         self.batch = batch
#     def publish_batch(self):
#         return f"The student is from batch {self.batch}"
# class student(Batch):
#     def __init__(self, name,batch):
#         self.name = name
#         #self.batch = batch
#         Batch.__init__(self, batch)
#     def publish_student(self):
#         return f"The student name is {self.name}"
#
# name = student('hemu','automation')
# print(name.publish_batch())
# print(name.publish_student())

#multiple inheritance  --> child gets features or methods from two or more parent
class A:
    def __init__(self,a):
        self.a = a
class B:
    def __init__(self,b):
        self.b = b
class Add(A,B):
    def __init__(self,a,b):
        A.__init__(self,a)
        B.__init__(self,b)
    def sum_of_num(self):
        total = self.a + self.b
        return f'add of num is {total}'
class Sub(A,B):
    def __init__(self,a,b):
        A.__init__(self,a)
        B.__init__(self,b)
    def sub_of_num(self):
        total = self.a - self.b
        return total
obj =Add(1,2)
print(obj.sum_of_num)

