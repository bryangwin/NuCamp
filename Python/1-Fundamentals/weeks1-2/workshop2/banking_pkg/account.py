def show_balance(balance):
    print(f"Current balance: ${balance:.2f}")
    
def deposit(balance):
    amount = float(input("Enter amount to despost: $"))
    return balance + amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: $"))
    if amount > balance:
        print("!!!Insufficient funds!!!")
        return balance
    else:
        return balance - amount
    
def logout(name):
    print(f"Goodbye {name}!")