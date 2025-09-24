import random
Selections = ["rock","paper","scissors"]
PC_choice = random.choice(Selections)
#print(PC_choice)

User_Input = input("Rock , Paper , Scissors Select?")
User_Input = User_Input.lower()

if User_Input not in Selections:
    print("Error")

if User_Input == "rock"  and PC_choice == "rock" :
    print("Draw")
elif User_Input == "paper"  and PC_choice == "paper" :
    print("Draw")
elif User_Input == "scissors"  and PC_choice == "scissors" :
    print("Draw")
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
    
#else:
  #print("Invalid entry")

