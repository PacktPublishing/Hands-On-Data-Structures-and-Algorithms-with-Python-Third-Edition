def selection_sort(unsorted_list):  
    size_of_list = len(unsorted_list)  
    for i in range(size_of_list):  
        small = i 
        for j in range(i+1, size_of_list):  
            if unsorted_list[j] < unsorted_list[small]:  
                small = j 
        temp = unsorted_list[i]  
        unsorted_list[i] = unsorted_list[small]  
        unsorted_list[small] = temp 

 


a_list = [3, 2, 35, 4, 32, 94, 5, 7] 

print("List before sorting", a_list) 

selection_sort(a_list) 

print("List after sorting", a_list) 
