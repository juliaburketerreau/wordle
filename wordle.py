#make sure on readme to tell users to download pip install rich in terminal
import random
from rich import print
from rich.color import Color
filehandle = open("words.txt", 'r')
print("Welcome to Wordle!")
print("download 'pip install rich' in the terminal before starting")
print("You have 6 tries to guess the 5 letter word")
print("Please enter your words below")
a = filehandle.readlines()
word = random.choice(a)
counter = 0
attempt = True
while attempt:
  counter = counter + 1
  if counter == 7:
    print("You did not get the wordle. The wordle was...", word)
    break
  guess = input('\n').lower()
  for i in range (min(len(guess), 5)):
      if guess[i] == word[i]:
        print("[green]" + (guess[i]) + "[/green]", end="")
      elif guess [i] in word:
        print("[yellow]" + (guess[i]) + "[/yellow]", end="")
      else:
        print(guess[i], end="")
      attempt = True
      if guess == word:
       print("[blue]\n" + "Congratulations! You got the wordle!" + "[/blue]\n", end="")
       attempt = False


    