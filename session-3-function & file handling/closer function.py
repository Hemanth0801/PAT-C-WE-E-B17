#closure funcction called as nexted function

def add(x):
    print(f"value of x is {x}")
    def wrapper(y):
        return x +y
    return wrapper(30)

print(add(1))

