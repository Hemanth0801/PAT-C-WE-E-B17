from random import randint
i=randint(1,10)
guess_number=input("Guess the number:")
while guess_number != i:
    print("Incorrect! number!")
    guess_number=input("Guess the number:")
print("Correct! number!")
