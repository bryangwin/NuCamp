

# def reverse(name):
#     return name[::-1]

def reverse(name):
    reversed_name = ""
    for char in name:
        reversed_name = char + reversed_name
    return reversed_name
    
# Or you could technically do this but I would not:
# reverse = lambda x: x[::-1]
    
    
name = input("What is your name? ")
print("Your name reversed is:", reverse(name))
