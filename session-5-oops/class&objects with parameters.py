class Dog:
    voice= "loud"

    def __init__(self, name):
        self.name = name        # init is a constructor used to install an object
    def bark(self):
        return f" {self.name} Bark {self.voice}"
    def sleeping(self):
        return("Sleep")
    def eaten(self):
        return f"yes {self.name} Eat"

shitz = Dog("Shitz")
print(shitz.eaten())
print(shitz.bark())
