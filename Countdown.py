import time

Duration= int(input("Enter duration amount: "))


countdown = [T for T in range(Duration,0,-1) ]
[print (f"{T}...") or time.sleep(1) for T in countdown]
print("TIME IS UP")
