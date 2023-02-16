username = input("Choose a username: [4-10 characters] ")

if 4 <= len(username) <= 10:
    print(f"Thank you. The username {username} is valid")
else:
    print("The username must be between 4 and 10 characters long")
    
