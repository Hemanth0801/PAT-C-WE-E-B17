import random
words = ['python', 'java', 'selenium', 'guvi']
word = random.choice(words)
scrambled = ''.join(random.sample(word, len(word)))
print("Unscramble this word:", scrambled)
guess = ""
while guess != word:
    guess = input("Enter your guess: ")
    if guess == word:
        print("Correct")
    else:
        print("Wrong guess. Try again")
