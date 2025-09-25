import math
Login_Details = ("mark ireri",1100000)
Selection = int(input ("***************************  \n Hello Welcome to KCB BANK \n Choose an option \n 1.Withdraw \n 2.Deposit \n 3.Show balance \n " 
"4.Exit\n ***************************\n =========>  " ))

balance_show= (10000)


if Selection == 1:
     Withdraw_Amount = int(input("\n enter amount to Withdraw : "))
     Withdraw_balance = balance_show - Withdraw_Amount
     print(f"You have Withdrawn {Withdraw_Amount} Ksh. YOUR BALANCE IS {Withdraw_balance}KSH ")

elif Selection == 2:
     user_deposit = float(input("\n Enter Amount to deposit:"))
     Deposit_balance = balance_show + user_deposit 
     print(f"You Have Deposited {user_deposit} Ksh. YOUR BALANCE IS {Deposit_balance}KSH ")

elif Selection == 3:
     print(balance_show)

elif Selection == 4:
     print("BYE!!!")

else:
     print("Invalid entry")
