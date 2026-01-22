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

#multiple inheritance
class mathoperation:
    def __init__(self, a, b):
        self.a = a

