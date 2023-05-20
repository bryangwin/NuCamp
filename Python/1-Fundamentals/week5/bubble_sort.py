unsorted_list = [101, 49, 3, 12, 56]

def bubble_sort(list):
    high_inx = len(list) - 1
    for i in range(high_inx):
        list_changed = False
        for j in range(high_inx):
            item = list[j]
            next = list[j+1]
            
            if item > next:
                list[j] = next
                list[j+1] = item
                list_changed = True
                
            print(list, i, j)
        if list_changed == False:
            break
    
bubble_sort(unsorted_list)