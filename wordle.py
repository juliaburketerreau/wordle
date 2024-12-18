import random
filehandle = open("words.txt", 'r')
print("Welcome to Wordle!")
print("You have 6 tries to guess the 5 letter word")
print("Please enter your words below")
a = filehandle.readlines()
word = random.choice(a)
for numguess in range (1,7):  
  guess = input().upper()
  if guess == a:
    print("Congratulations!")
    break
  else:
    continue









