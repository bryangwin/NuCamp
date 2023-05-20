import time
import json

with open("stories.json", "r") as file:
    stories = json.load(file)


print("Welcome to Mad Libs!")

# Have the user choose a story topic.
while True:
    print("\nPlease choose from the list of the following topics:\n")

    for key in stories:
        print(key)

    choice = input("\nType your choice: ").title()

    if choice not in stories:
        print("\nThat is not a valid option. Please check your spelling and try again.")
        time.sleep(3)
    else:
        break

story_data = stories[choice]

# Collect user inputs
user_inputs = {}
for placeholder in story_data["placeholders"]:
    user_inputs[placeholder] = input(f"Please enter a {placeholder.replace('_', ' ').title()}: ")

# Replace the placeholders with user inputs:
story = story_data["template"].format(**user_inputs)

# Print the Mad Lib story
print("Alright! Your Mad Lib story is cooking and will be coming out in...")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("\nHere is your Mad Libs story!")
print(story)
        