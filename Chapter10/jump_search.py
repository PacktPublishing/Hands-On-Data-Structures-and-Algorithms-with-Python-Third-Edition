def search_ordered(ordered_list, term):   
    print("Entering Linear Search") 
    ordered_list_size = len(ordered_list)   
    for i in range(ordered_list_size):   
        if term == ordered_list[i]:   
            return i   
        elif ordered_list[i] > term:   
            return -1   
    return -1



def jump_search(ordered_list, item): 
    import math
    print("Entering Jump Search") 
    list_size = len(ordered_list)                           
    block_size = int(math.sqrt(list_size))          
    i = 0                                
    while i != len(ordered_list)-1 and ordered_list[i] <= item: 
        print("Block under consideration - {}".format(ordered_list[i: i+block_size])) 
        if i+ block_size > len(ordered_list): 
            block_size = len(ordered_list) - i 
            block_list = ordered_list[i: i+block_size] 
            j = search_ordered(block_list, item) 
            if j == -1: 
                print("Element not found") 
                return  
            return i + j 
        if ordered_list[i + block_size -1] == item:            
            return i+block_size-1 
        elif ordered_list[i + block_size - 1] > item:            
            block_array = ordered_list[i: i + block_size - 1] 
            j = search_ordered(block_array, item) 
            if j == -1: 
                print("Element not found") 
                return   
            return i + j 
        i += block_size



print(jump_search([1,2,3,4,5,6,7,8,9, 10, 11], 8))

