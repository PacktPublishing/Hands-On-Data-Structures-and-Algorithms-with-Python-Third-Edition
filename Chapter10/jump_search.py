def search_ordered(ordered_list, term):   
    print("Entering Linear Search") 
    ordered_list_size = len(ordered_list)   
    for i in range(ordered_list_size):   
        if term == ordered_list[i]:   
            return i   
        elif ordered_list[i] > term:   
            return -1   
    return -1



def jump_search(A, item): 
    print("Entering Jump Search") 
    n = len(A)                           
    m = int(math.sqrt(n))          
    i = 0                                
    while i != len(A)-1 and A[i] <= item: 
        print("Block under consideration - {}".format(A[i: i+m])) 
        if i+m > len(A): 
            m =  len(A) - i 
            B = A[i: i+m] 
            j = search_ordered(B, item) 
            if j == -1: 
                print("Element not found") 
                return  
            return i + j 
        if A[i+m-1] == item:            
            return i+m-1 
        elif A[i+m-1] > item:            
            B = A[i: i+m-1] 
            j = search_ordered(B, item) 
            if j == -1: 
                print("Element not found") 
                return    
            return i + j 
        i += m



print(jump_search([1,2,3,4,5,6,7,8,9, 10, 11], 10))

