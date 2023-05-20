def binary_search(list, target):
    lower_bound = 0
    upper_bound = len(list) -1
    
    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = list[pivot]
        
        if pivot_value == target:
            return pivot
        if pivot_value > target:
            upper_bound = pivot -1
        else:
            lower_bound = pivot +1
            
    return -1

list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]

print(binary_search(list, 10))

print(binary_search(list, 4))