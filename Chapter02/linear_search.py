# Linear search program to search an element, return the index position of the #array  

def searching(search_arr, x):
    for i in range(len(search_arr)):
        if search_arr[i] == x:            
            return i       
    return -1


search_arr = [3, 4, 1, 6, 14]  
x=4
print("Index position for the element x is:", searching(search_arr, x)) 
