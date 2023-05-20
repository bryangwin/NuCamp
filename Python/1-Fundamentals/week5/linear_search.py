def linear_search(list, target):
    for x in range(len(list)):
        if list[x] == target:
            print(f"Found at index: {x}")
            return x
    print("Target is not in the list")
    return -1

list = [5, 4, 6, 2, 3]

linear_search(list, 8)        
    