def binary_search_iterative(ordered_list, term):  
 
    size_of_list = len(ordered_list) - 1  
    index_of_first_element = 0  
    index_of_last_element = size_of_list  
    while index_of_first_element <= index_of_last_element:  
        mid_point = (index_of_first_element + index_of_last_element)/2  
        if ordered_list[mid_point] == term:  
            return mid_point  
        if term > ordered_list[mid_point]:  
            index_of_first_element = mid_point + 1  
        else:  
            index_of_last_element = mid_point - 1  
    if index_of_first_element > index_of_last_element:  
        return None             
            
store = [1, 4, 5, 12, 43, 54, 60, 77]
a = binary_search_iterative(store, 2)
print("Index position of value 2 is", a)


print(binary_search_iterative(store, 7))  

print(binary_search_iterative(store, 60))  


list1 = [10, 30, 100, 120, 500]

search_term = 10
index_position1 = binary_search_iterative(list1, search_term)
if index_position1 is None:
    print("The data item {} is not found".format(search_term))
else:
    print("The data item {} is found at position {}".format(search_term, index_position1))


list2 = ['book','data','packt', 'structure']

search_term2 = 'structure'
index_position2 = binary_search_iterative(list2, search_term2)
if index_position2 is None:
    print("The data item {} is not found".format(search_term2))
else:
    print("The data item {} is found at position {}".format(search_term2, index_position2))
