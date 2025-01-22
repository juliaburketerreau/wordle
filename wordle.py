#make sure on readme to tell users to download pip install rich in terminal
import random
from rich import print
from rich.color import Color
#instructions
filehandle = open("words.txt", 'r')
print("Welcome to Wordle!")
print("download 'pip install rich' in the terminal before starting")
print("How to play:")
print("if the letter turns [green] green [/green], the letter [blue]is[/blue] in the right place.")
print("if the letter turns [yellow] yellow [/yellow], the letter [blue]is[/blue] in the word, but in the wrong place")
print("if the letter is white, the letter is [red]not[/red] in the word")
print("You have 6 tries to guess the 5 letter word")
print("Please enter your words below")
#reads the file, then chooses a random word using an array, that word is now the wordle
a = filehandle.readlines()
word = random.choice(a).strip()
#sets counter for number of tries
counter = 0
attempt = True
#this loop begins with error checking, and then it checks if the word is correct, or if it has been more than 6 guesses and the word is still incorrect
while attempt:
  guess = (input('\n').lower()) 
  try:
    int(guess)
    print('invaild guess')
  except:
    counter = counter + 1
    if guess == word:
      print("[blue]" + "Congratulations! You got the wordle in " + str(counter) + " guess/guesses!" + "[/blue]", end="")
      break
      
    elif guess != word and counter == 6:
      print("You did not get the wordle. The wordle was...", word)
      attempt = False
#this loop is the most important, and it changes the colour of the letters. 
#it checks to see if the letters match up (green), if the letter is in the word (yellow) and if the letter is not in word (gray)
  for i in range (min(len(guess), 5)):
        if guess[i] == word[i]:
          print("[green]" + (guess[i]) + "[/green]", end="")
        elif guess [i] in word:
          print("[yellow]" + (guess[i]) + "[/yellow]", end="")
        else:
          print(guess[i], end="")