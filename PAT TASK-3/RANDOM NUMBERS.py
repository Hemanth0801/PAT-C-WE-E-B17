import random
num=random.randint(1, 10)  #randint is used to choose the random num
print("Guess a number between 1 and 10")
while True:                            #loop
    i = int(input("Enter your guess: "))  #input data we need to  enter
    if i < num:
        print("Too low! Try again.")     #if i value is less than ramdom num
    elif i > num:
        print("Too high! Try again.")     #f i value is greater than ramdom num
    else:
        print("Correct! You guessed the number!")     #else means thers is only option "="
        break