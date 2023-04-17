from banking_pkg import account

balance = 0.0


def atm_menu(name):
    """Show the ATM Menu with options"""

    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")

while True:
    name = input("Enter name to register: ")
    if len(name) > 10:
        print("Name must not exceed 10 characters.")
    else:
        break

while True:
    pin = input("Enter PIN: ")
    if len(pin) != 4 or not pin.isdigit():
        print("PIN must be 4 characters and all numbers")
    else:
        break
    
print(f"{name} has been registered with balance of: ${balance:.2f}")

print("LOGIN")

while True:
    login_name = input("Enter Name: ")
    login_pin = input("Enter PIN: ")
    if login_name != name or login_pin != pin:
        print("Invalid Credentials. Try again.")
    else:
        break

while True:
    atm_menu(name)
    choice = input("Choose a selection. Type a number between 1 and 4: ")
    if choice == "1":
        account.show_balance(balance)
    elif choice == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif choice == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif choice == "4":
        account.logout(name)
        break
    else:
        print("That is not a valid entry.")
