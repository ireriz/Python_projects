import random

Selections = ("rock","paper","scissors")
PC_choice = random.choice(Selections)

User_Input = input("Rock , Paper , Scissors Select?")
User_Input = User_Input.lower()

if User_Input not in Selections:
    message = print("Error Invalid Selection")
else:
   print("")

while True:
 
 if User_Input == PC_choice: 
    print(f"Draw I also chose {User_Input}")
 elif User_Input == "rock" and PC_choice == "paper":
    print("User has won")
 elif User_Input == "paper" and PC_choice == "rock":
    print("PC has won")
 elif User_Input == "scissors" and PC_choice == "paper":
    print("User has won")
 elif User_Input == "paper" and PC_choice == "scissors":
    print("PC has won")
 elif User_Input == "rock" and PC_choice == "scissors":
    print("User has won")
 elif User_Input == "scissors" and PC_choice == "rock":
    print("PC has won")
 break

print(f"I chose {PC_choice}")
