def show_homepage():
    print("")
    print("          === DonateMe Homepage ===        ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.      Register      |")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.   Show Donations   |")
    print("------------------------------------------")
    print("|               5. Exit                   |")
    print("------------------------------------------\n")

total_donation_amount = 0


def donate(username):
    amount = float(input("Enter amount to donate: $"))
    string = f"{username} donated ${amount:.2f}"
    print (f"Thank you for you donation of ${amount:.2f}!")
    global total_donation_amount
    total_donation_amount += amount
    return string

def show_donations(donations):
    print("\n--- All Donations ---")
    if len(donations) == 0:
        print("Currently no donations.")
    else:
        for amounts in donations:
            print(amounts)
        print(f"Total amount donated: ${total_donation_amount:.2f}")
    