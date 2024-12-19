import random
filehandle = open("words.txt", 'r')
print("Welcome to Wordle!")
print("You have 6 tries to guess the 5 letter word")
print("Please enter your words below")
a = filehandle.readlines()
word = random.choice(a)
for numguess in range (1,7):  
  guess = input().lower()
  if len(guess) > 5:
   print("5 letter words only")
  elif len(guess) < 5:
   print("5 letter words only")

for i in range (min (len(guess), 5)) and (max (len(guess), 5)):
  if guess[i] == word[i]:
    print(colored(guess[i], 'green'), end="")
  elif guess [i] in word:
    print(colored(guess[i], 'yellow'), end="")
  else:
    print(guess[i], end="")

  if guess == word:
    print("Congratulations!")