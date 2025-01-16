#make sure on readme to tell users to download pip install rich in terminal
import random
from rich import print
from rich.color import Color
filehandle = open("words.txt", 'r')
print("Welcome to Wordle!")
print("download 'pip install rich' in the terminal before starting")
print("How to play:")
print("if the letter turns [green] green [/green], the letter is in the right place.")
print("if the letter turns [yellow] yellow [/yellow], the letter is in the word, but in the wrong place")
print("if the letter is white, the letter is not in the word")
print("You have 6 tries to guess the 5 letter word")
print("Please enter your words below")
a = filehandle.readlines()
word = random.choice(a)
counter = 0
attempt = True
while attempt:
  guess = input('\n').lower()     
  counter = counter + 1
  if guess == word:
      print("[blue]" + "Congratulations! You got the wordle in " + str(counter) + " guess/guesses!" + "[/blue]", end="")
      attempt = False
  if guess != word and counter == 6:
    print("You did not get the wordle. The wordle was...", word)
    attempt = False
  for i in range (min(len(guess), 5)):
      if guess[i] == word[i]:
        print("[green]" + (guess[i]) + "[/green]", end="")
      elif guess [i] in word:
        print("[yellow]" + (guess[i]) + "[/yellow]", end="")
      else:
        print(guess[i], end="")