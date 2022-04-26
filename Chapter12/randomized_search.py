def partition(unsorted_array, first_index, last_index):

    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index

    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index + 1

    while True:

        while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1
        while unsorted_array[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
            less_than_pivot_index -= 1

        if greater_than_pivot_index < less_than_pivot_index:
            temp = unsorted_array[greater_than_pivot_index]
            unsorted_array[greater_than_pivot_index] = unsorted_array[less_than_pivot_index]
            unsorted_array[less_than_pivot_index] = temp
        else:
            break

    unsorted_array[pivot_index] = unsorted_array[less_than_pivot_index]
    unsorted_array[less_than_pivot_index] = pivot

    return less_than_pivot_index
  
  
def quick_select(array_list, start, end, k): 
    split = partition(array_list, start, end) 
    if split == k: 
        return array_list[split] 
    elif split < k: 
        return quick_select(array_list, split + 1, end, k) 
    else: 
        return quick_select(array_list, start, split-1, k) 




list1 = [3,1,10, 4, 6, 5] 

print("The 2nd smallest element is", quick_select(list1, 0, 5, 1)) 

print("The 3nd smallest element is", quick_select(list1, 0, 5, 2)) 

 


stored = [3,1,10,4,6,5]
print(stored)
print(quick_select(stored, 0, 5, 0))
stored = [3,1,10,4,6, 5]
print(quick_select(stored, 0, 5, 1))
stored = [3,1,10,4,6, 5]
print(quick_select(stored, 0, 5, 2))
stored = [3,1,10,4,6, 5]
print(quick_select(stored, 0, 5, 3))
stored = [3,1,10,4,6, 5]
print(quick_select(stored, 0, 5, 4))
stored = [3,1,10,4,6, 5]
print(quick_select(stored, 0, 5, 5))
