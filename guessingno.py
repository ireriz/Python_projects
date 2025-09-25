
import random

num_to_guess = random.randint(1,100)
print(num_to_guess)

user_guess = int(input("Enter a number btwn 1-100: "))

while True:
    if user_guess > num_to_guess:
        print("too high! Guess a lower number")
        user_guess = int(input("Enter a number btwn 1-100: "))
    elif user_guess < num_to_guess:
        print("too low! Guess a higher number")
        user_guess = int(input("Enter a number btwn 1-100: "))
        
    else:
        print("congrats you guessed the number")
        break
        

