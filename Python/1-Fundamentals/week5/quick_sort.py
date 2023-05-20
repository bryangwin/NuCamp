list = [5, 4, 1, 2, 3]

def sort_part(list, low_idx, pivot_idx):
    pivot_val = list[pivot_idx]
    
    while pivot_idx != low_idx:
        low_val = list[low_idx]
        print(list, low_val, pivot_val)
        if low_val <= pivot_val:
            low_idx += 1
        else:
            list[low_idx] = list[pivot_idx-1]
            list[pivot_idx] = low_val
            list[pivot_idx-1] = pivot_val
            pivot_idx -= 1
            
    return pivot_idx
    

def quick_sort(list, low_idx, high_idx):
    if low_idx > high_idx:
        return
    pivot_idx = sort_part(list, low_idx, high_idx)
    quick_sort(list, low_idx, pivot_idx-1)
    quick_sort(list, pivot_idx+1, high_idx)
    
quick_sort(list, 0, len(list)-1)