from donations_pkg import homepage, user

database ={
    "admin": "password123",
    }

donations = []
authorized_user = ""

while True:
    homepage.show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as {authorized_user}")

    user_choice = input("Choose an option. Type a number between 1 and 5: ")
    if user_choice == "1":
        username = input("Enter your username: ").lower()
        password = input("Enter your password: ")
        authorized_user = user.login(database, username, password)
    elif user_choice == "2":
        while True:
            username = input("Enter a username to register: ").lower()
            if len(username) > 10:
                print("Username cannot be over 10 characters.")
            else:
                break
        while True:
            password = input("Enter a password: ")
            if len(password) < 5:
                print("Password but be at least 5 characters.")
            else:
                break
        authorized_user = user.register(database, username)
        if authorized_user != "":
            database[username] = password
        
    elif user_choice == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donate_string = homepage.donate(authorized_user)
            donations.append(donate_string)
    elif user_choice =="4":
        homepage.show_donations(donations)
    elif user_choice == "5":
        print(" Leaving DonateMe...")
        break
    else:
        print("That is not a valid input.")