import random

def guess_random_number(tries, start, stop):
    randnum = random.randint(start, stop)
    guessed_nums = set()
    while tries != 0:
        print(f"{tries} tries remaining.")
        while True:
            guess = int(input(f"Guess a number between {start} and {stop}: "))
            if guess < start or guess > stop:
                print("That is not a valid entry.")
            elif guess in guessed_nums:
                print("You already guessed that number.")
            else:
                guessed_nums.add(guess)
                break
        
        if guess == randnum:
            print("You got it!")
            return
        elif guess < randnum:
            print("The number is higher.")
            tries -= 1
        elif guess > randnum:
            print("The number is lower.")
            tries -= 1
            
    print(f"Game Over. The number was {randnum}")
    return

def guess_random_num_linear(tries, start, stop):
    randnum = random.randint(start, stop)

    for x in range(start, stop + 1):
        if tries == 0:
            print("The computer has failed to guess the number.")
            return 2
        print(f"The number for the computer to guess is: {randnum}")
        print(f"Number of tries left: {tries}")
        print(f"The computer is guessing... {x}")
        tries -= 1
        if x == randnum:
            print("The program has guess the the correct number!")
            return 1

def guess_random_num_binary(tries, start, stop):
    randnum = random.randint(start, stop)
    print(f"Random number to find: {randnum}")
    lower_bound = start
    upper_bound = stop
    
    while tries != 0:
        pivot = (lower_bound + upper_bound) // 2
        
        if pivot == randnum:
            print(f"The computer found it! {randnum}")
            return
        if pivot > randnum:
            print("The computer is guessing lower!")
            upper_bound = pivot -1
            tries -= 1
        else:
            print("The computer is guessing higher!")
            lower_bound = pivot +1
            tries -= 1
            
    print("The computer failed to find the number.")
    return
            
def guess_random_num():
    tries = int(input("Enter number of tries for the guessing game: "))
    start = int(input("Enter the low number for the range of numbers: "))
    stop = int(input("Enter the high number for the range of numbers: "))
    while True:
        user_choice = input("""
Choose the type of game to play:
1. User Input
2. Linear Search
3. Binary Search
Enter a number 1 - 3 to choose: """)
        if user_choice == "1":
            guess_random_number(tries, start, stop)
            break
        elif user_choice == "2":
            guess_random_num_linear(tries, start, stop)
            break
        elif user_choice == "3":
            guess_random_num_binary(tries, start, stop)
            break
        else:
            print("That is not a valid entry.")
        
def gambling_game():
    money = 10
    while money > 0 and money < 50:
        print(f"You have ${money} left in your bank.")
        while True:
            bet = int(input("Hou much money would you like to bet?: $ "))
            if bet > money:
                print("You don't have the much money in the bank.")
            else: 
                break
        while True:    
            guess = int(input("Do you think the computer will get the number? Enter 1 for yes, 2 for no."))
            if guess == 1 or guess == 2:
                break
            else:
                print("That is not a valid entry.")
        if guess == guess_random_num_linear(5, 1, 10):
            print("You won!")
            money += bet
            
        else:
            print("You lost...")
            money -= bet
            
    if money <= 0:
        print("You lost all your money... Game Over")
        return
    elif money >= 50:
        print("You made it to $50! You Win!")
        return

                
        
    
      
# Driver Code 1
# guess_random_number(5, 1, 10)

# Driver Code 25
# guess_random_num_linear(5, 1, 10)

# Diver Code 3
# guess_random_num_binary(5, 0, 100)

# Driver Code 4
# guess_random_num()

# Driver Code 5
# gambling_game()