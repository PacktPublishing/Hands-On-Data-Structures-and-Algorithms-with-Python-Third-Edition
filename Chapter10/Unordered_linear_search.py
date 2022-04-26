
def search(unordered_list, term):
    for i, item in enumerate(unordered_list):
        if term == unordered_list[i]:
            return i
    return None



list1 = [60, 1, 88, 10, 11, 600] 

search_term = 10 
index_position = search(list1, search_term)  
print(index_position) 

 

list2 = ['packt', 'publish', 'data'] 
search_term2 = 'data' 
index_position2 = search(list2, search_term2) 
print(index_position2)


if index_position is None:
    print("{} not found".format(search_term))
else:
    print("{} found at position {}".format(search_term, index_position))


if index_position2 is None:
    print("{} not found".format(search_term2))
else:
    print("{} found at position {}".format(search_term2, index_position2))
