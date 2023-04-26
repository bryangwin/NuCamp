numbers = {1, 2, 3, 4, 5, 5, 5,}

print(numbers)

words_set = {"Dog", "Goose", "Bird"}

for word in words_set:
    print(word)
    
words_set.add("Brick")

print(words_set)

words_set.discard("Dog")

print(words_set)