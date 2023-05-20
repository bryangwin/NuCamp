class User:
    def __init__(self, name, pin, password) -> None:
        self.name = name
        self.pin = pin
        self.password = password
        
    def change_name(self, new_name):
        if len(new_name) >=2 and new_name != self.name:
            self.name = new_name
        else:
            print("Username must be at least 2 characters long and cannot be the same as old username.")
        
    def change_pin(self, new_pin):
        if len(str(new_pin)) == 4 and new_pin != self.pin:
            self.pin = new_pin
        else:
            print("PIN must be 4 characters long and cannot be the same as old PIN.")
        
    def change_password(self, new_password):
        if len(new_password) >= 5 and new_password != self.password:
            self.password = new_password
        else:
            print("Password must be at least 5 characters and cannot be the same as old password.")
        
        
class BankUser(User):
    def __init__(self, name, pin, password) -> None:
        super().__init__(name, pin, password)
        self.balance = 0
        self.on_hold = False

    def show_balance(self):
        print(f"{self.name} has a balance of: ${self.balance:.2f}")

    def withdraw(self, amount):
        if self.on_hold == True:
            print("Your account is on hold. Transaction denied.")
        else:
            if isinstance(amount, int) or isinstance(amount, float):
                if amount > -1:
                    if amount <= self.balance:
                        self.balance -= amount
                        return self.balance 
                    else:
                        print("Insufficient funds.")
                else:
                    print("Withdraw amount must be a positive number. Transaction cancelled.")
            else:
                print("Amount must be a number.")
        
    def deposit(self, amount):
        if self.on_hold == True:
            print("Your account is on hold. Transaction denied.")
        else:
            if isinstance(amount, int) or isinstance(amount, float):
                if amount > -1:
                    self.balance += amount
                    return self.balance
                else:
                    print("Deposit amount must be a positive number. Transaction cancelled.")
            else:
                print("Amount must be a number.")
            
    def transfer_money(self, amount, user):
        if self.on_hold == True:
            print("Your account is on hold. Transaction denied.")
        else:
            print(f"\nYou are transferring ${amount:.2f} to {user.name}.")
            print("Authentication required")
            pin = int(input("Enter your pin: "))
            if pin == self.pin:
                print(f"Transferring ${amount} to {user.name}")
                self.withdraw(amount)
                user.deposit(amount)
                return True
            else:
                print("Invalid PIN, transaction cancelled.")
                return False
                
    def request_money(self, amount, user):
        if self.on_hold == True:
            print("Your account is on hold. Transaction denied.")
        else:
            print(f"\nYou are requesting ${amount:.2f} from {user.name}")
            pin = int(input("Enter payers PIN: "))
            if pin == user.pin:
                password = input("Enter your password: ")
                if password == self.password:
                    print("Request Auhtorized")
                    user.withdraw(amount)
                    self.deposit(amount) 
                    print(f"{user.name} sent ${amount} ")
                    return True
                else:
                    print("Invalid password, transaction cancelled.")
                    return False
            else:
                print("Invalid PIN, transaction cancelled.")
                return False
            
        
    def toggole_on_hold(self):
        if self.on_hold == True:
            self.on_hold = False
        elif self.on_hold == False:
            self.on_hold = True
        
        
        
    
        

# # Driver Code 1:

# user1 = User("Bob", 1234, "password")

# print(f"{user1.name} {user1.pin} {user1.password}")


#Driver Code 2:

# user1 = User("Bob", 1234, "password")

# print(f"{user1.name} {user1.pin} {user1.password}")

# user1.change_name("Bobny")
# user1.change_password("newpass")
# user1.change_pin(2345)

# print(f"{user1.name} {user1.pin} {user1.password}")


#Driver Code 3:

# bankuser1 = BankUser("James", 1234, "password")

# print(f"{bankuser1.name} {bankuser1.pin} {bankuser1.password} {bankuser1.balance}")


#Driver Code 4:

# bankuser1 = BankUser("James", 1234, "password")

# print(f"{bankuser1.name} {bankuser1.pin} {bankuser1.password} {bankuser1.balance}")

# bankuser1.show_balance()
# bankuser1.deposit(300)
# bankuser1.show_balance()
# bankuser1.withdraw(300)
# bankuser1.show_balance()


# Driver Code 5:

alice = BankUser("Alice", 1234, "password")
bruce = BankUser("Bruce", 1234, "password1")

bruce.deposit(5000)

alice.show_balance()
bruce.show_balance()

if bruce.transfer_money(123, alice):
    alice.show_balance()
    bruce.show_balance()
    bruce.request_money(250, alice)

alice.show_balance()
bruce.show_balance()