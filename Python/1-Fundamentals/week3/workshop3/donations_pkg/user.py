def login(database, username, password):
    if username in database and database[username] == password:
        print(f"Welcome back {username}.")
        return username
    elif username in database and not database[username] == password:
        print("Incorrect password.")
        return ""
    else:
        print("Username not found.")
        return ""
        
def register(database, username):
    if username in database:
        print("That username is already taken.")
        return ""
    else:
        print(f"{username} has been registered.")
        return username
    

    