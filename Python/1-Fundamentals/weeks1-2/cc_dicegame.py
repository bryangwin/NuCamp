import random

score = 0


def dice_game():
    global score
    print(f"Current High Score: {score}")
    print("1. Roll Dice")
    print("2. Leave Game")
    choice = input("Enter your choice: ")
    if choice == "1":
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        sum_dice = dice_one + dice_two
        print(f"\nYou roll a... {dice_one}")
        print(f"You roll a... {dice_two}\n")
        print(f"You have rolled a total of: {sum_dice}\n")
        if sum_dice > score:
            score = sum_dice
            print("New High Score!\n")
        dice_game()
    else:
        print("Goodbye!")

if __name__ == '__main__':
    dice_game()
