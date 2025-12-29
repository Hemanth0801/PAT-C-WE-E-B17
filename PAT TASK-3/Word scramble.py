import random
words = ['python','javascript','java','automation','pytest','guvi','selenium']
random_word = random.choice(words)  #it will choose random word from the list
letters= list(random_word)
random.shuffle(letters)     #shuffle the selected word
scrambled_word = ''.join(letters)    #shuffled word get joined
print("scrambled_word: ", scrambled_word)
while True:
    guess = input("Guess a letter: ")
    if guess == random_word:     #if guess correct loop will break or else it will continue
        print("Correct!")
        break
    else:
        print("Incorrect!, try again.")

