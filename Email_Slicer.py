
Email_add = input("Enter your full Email Address below : \n ---->")

username, hostname = [char for char in Email_add.split ("@")]
print (f"username: {username}")
print(f"hostname: {hostname} \n ")