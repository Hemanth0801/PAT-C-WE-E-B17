# opps = object oriented programinning

#classes and object
#classes are called as blue print -> car is a concept
   # method = steering,wheels,gearbox,engine,etc
   # class have attributes , which features like colour,alloy wheels etc
   #example : 1
class car:
    def steering(self):
        return( "Steer")       # #self refers to a class
    def brake(self):
        return("Brake")
    def throwing(self):
        return("Throwing")

print(car().steering())  #caris class and ,method()

#example : 2
#dog are also type of classes
#methods : braking, sleep,walk,run,eat
#attribute: colour
class Dog:
    def bark(self):
        return("Bark")
    def sleeping(self):
        return("Sleep")
    def eaten(self):
        return("Eat")
print(Dog().eaten())

#objects
#objects are protype which  are called instances of class
#obbject acces the method of a classes
#oject have their own identity --> object have unique name
#object have attribute , which could be behaviour or indivial trait

sedan = car()   #sedan is an instances of a class(car)
sedan.steering()    # . operator will help to acess method of a  class

suv = car()   #suv is an instances of a class(car)
suv.steering() # . operator will help to acess method of a  class

