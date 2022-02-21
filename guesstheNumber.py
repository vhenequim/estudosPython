import random

def check_num(guess, randnum):
  if guess == randnum:
    print ("Right awnser!")
    return 1
  elif guess > randnum:
    print ("Too high")
  else:
    print ("Too low")

def guess_game():
  number = random.randint(1, 100)
  print (number)
  if input("Guess the number from 1 to 100! Which difficulty do you want? 'hard' or 'easy'? ") == "hard":
    attempt = 5
  else:
    attempt = 10
  while attempt:
    guess = int (input (f"Attempt lefts:{attempt} \nGuess: "))
    if check_num(guess, number):
      print ("You won!")
      return 0
    else:
      attempt = attempt - 1
  print ("You couldn't make it :(")
  return 0

key = True
while key:
  guess_game()
  if input ("Whanna try again?'y' or 'n'") == 'n':
    key = False
    print ("Bye")
