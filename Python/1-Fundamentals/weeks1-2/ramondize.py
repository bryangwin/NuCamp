import random

dice_roll = random.randint(1, 6)

print(f"Your dice roll is {dice_roll}")

prize = ["dong", "$100,000", "Pony", "$1,000,000"]

print(f"Your random prize is {random.choice(prize)}")

random.shuffle(prize)
print(prize)