#make sure on readme to tell users to download pip install rich in terminal
import random
from rich import print
from rich.color import Color
filehandle = open("words.txt", 'r')
print("Welcome to Wordle!")
print("download pip install rich in the terminal before starting")
print("You have 6 tries to guess the 5 letter word")
print("Please enter your words below")
a = filehandle.readlines()
word = "tests"
#word = random.choice(a)
redo = True
while redo:
  for numguess in range (1,7):  
    guess = input().lower()
    if len(guess) > 5:
      print("5 letter words only")
    elif len(guess) < 5:
      print("5 letter words only")
    redo = True
    if len(guess) == 5:
      redo = False
      break
redo = True
while redo:
 for i in range (len(guess)):
  if guess[i] == word[i]:
    print("[green]" + (guess[i]) + "[/green]", end="")
  elif guess [i] in word:
    print("[yellow]" + (guess[i]) + "[/yellow]", end="")
  else:
    print(guess[i], end="")
  redo = True
  if guess == word:
    print("Congratulations!")
  redo = False