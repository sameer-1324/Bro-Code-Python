username = input("Enter your username: ")

if len(username) > 12:
    print("Your username is too long")
elif not username.find(" ") == -1:
    print("Your username cant contain spaces")
elif not username.isalpha():
    print("Your username cant contain numbers")
else:
    print(f"Wlecome {username}")