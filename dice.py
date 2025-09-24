#HERE IS A DICE GAME

import random 

Choice = input("Do you want to roll the dice? (y/n): ")
Choice = Choice.capitalize()

while True:
 Choice = Choice.capitalize()

 if Choice == "Y":
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    print(f"({num1}, {num2})")
    Choice = input("Do you want to roll the dice? (y/n): ")
 
 elif not Choice == "N":
    print ("invalid selection")
    Choice = input("Do you want to roll the dice? (y/n): ")

 else:
    print("Thank you for playing")

    break


 