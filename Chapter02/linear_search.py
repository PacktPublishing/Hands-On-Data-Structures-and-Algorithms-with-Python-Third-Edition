# Linear search program to search an element, return the index position of the #array  

def linear_search(input_list, element):
    for index, value in enumerate(input_list):
        if value == element:
            return index
        
    return -1

 
input_list = [3, 4, 1, 6, 14]  
element = 4
print("Index position for the element x is:", linear_search(input_list,element)) 
