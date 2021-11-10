def binary_search(arr, low, high, key):
    while low <= high:
        mid = int(low + (high - low)/2)  
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1  


arr = [ 2, 3, 4, 2, 10, 40] 
x = 10 
result = binary_search(arr, 0, len(arr)-1, x)  
print(result)
