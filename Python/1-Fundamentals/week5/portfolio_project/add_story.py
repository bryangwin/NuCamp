import json
import re

def add_story(name: str, template: str):
    """
    Use to add a new story to the stories.json file.

    Both parameters will be strings.

    name = the name of the string and the key for the dictionary item.

    template = the story. Be sure to put your placeholders inside of {}

    placeholders must be one word.
    """
    # Load the existing JSON data
    with open("stories.json", "r") as infile:
        stories = json.load(infile)

    # Extract placeholders from the template using a regular expression
    placeholders = re.findall(r"{(\w+)}", template)

    # Add the new story entry to the stories dictionary
    stories[name.title()] = {
        "template": template,
        "placeholders": placeholders
    }

    # Write the updated dictionary back to the JSON file
    with open("stories.json", "w") as outfile:
        json.dump(stories, outfile, indent=4)

# Example usage
add_story("New Story", "This is a {adjective} story about a {noun}.")

