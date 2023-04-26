import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:

    user_choice = input("Press enter to pick a card, or Q then enter to quit: ").lower()
    if user_choice == "q":
        print("Goodbye!")
        break
    else:
        random_card_index = random.randint(0, len(diamonds)-1)
        card_chosen = diamonds.pop(random_card_index)
        hand.append(card_chosen)
        print(f"Your hand: {hand}")
        print(f"Remaining cards: {diamonds}")
    
if not diamonds:
    print("There are no more cards to pick.")


