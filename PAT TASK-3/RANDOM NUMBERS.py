import random
num=random.randint(1, 10)
print("Guess a number between 1 and 10")
while True:
    i = int(input("Enter your guess: "))
    if i < num:
        print("Too low! Try again.")
    elif i > num:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed the number!")
        break