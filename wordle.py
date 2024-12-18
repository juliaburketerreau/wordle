import random
filehandle = open("words.txt", 'r')
print("Welcome to Wordle!")
print("You have 5 tries to guess a 5 letter word")

a = filehandle.readlines()
print(random.choice(a))

