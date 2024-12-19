import random
from termcolor import color
filehandle = open("words.txt", 'r')
print("Welcome to Wordle!")
print("You have 6 tries to guess the 5 letter word")
print("Please enter your words below")
a = filehandle.readlines()
word = random.choice(a)
for numguess in range (1,7):  
  guess = input().upper()
  if len(guess) == 5:
    continue
  else:
      print("word must be five letters")
  if guess == a:
    print("Congratulations!")
    break
  else:
    continue

for i in range (guess):
  if guess[i] == word[i]:
    print(colored(guess[i] 'green'), end="")
  elif guess [i] in word:
    print(colored(guess[i] 'yellow'), end="")
  else:
    print(guess[i], end="")