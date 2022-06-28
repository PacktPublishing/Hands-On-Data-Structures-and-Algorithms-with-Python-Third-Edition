def binary_search_recursive(ordered_list, first_element_index, last_element_index, term):    
    if (last_element_index < first_element_index):   
        return None   
    else:   
        mid_point = first_element_index + ((last_element_index - first_element_index) // 2)   
        if ordered_list[mid_point] > term:   
            return binary_search_recursive (ordered_list, first_element_index, mid_point-1, term)   
        elif ordered_list[mid_point] < term:   
            return binary_search_recursive (ordered_list, mid_point+1, last_element_index, term)   
        else:   
            return mid_point





def exponential_search(A, search_value): 
    if (A[0] == search_value): 
        return 0     
    index = 1 
    while index < len(A) and A[index] < search_value: 
        index *= 2        
    return binary_search_recursive(A, index // 2, min(index, len(A) - 1), search_value) 




print(exponential_search([1,2,3,4,5,6,7,8,9,10,11,12,34,40],34)) 
