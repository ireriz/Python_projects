# number guessing game

import random
MAX = 100
random.seed()
numtoguess = random.randint(1, 100)

while True:

  try:
    guess = int(input("guess the number btwn 1-100: "))
    if guess < numtoguess:
      print("too low")
    elif guess < numtoguess:
        ("too high")
    elif guess > MAX:
       print("pick a number below 100")
    else:
        print("CONGRATS")
        break

  except ValueError:
    print("enter valid  btwn 1-100")
