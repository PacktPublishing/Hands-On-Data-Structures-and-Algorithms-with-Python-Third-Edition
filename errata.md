# Errata, Corrections and Improvements
----------------------------------------------------
If you find any mistakes in the third edition of Hands On Data Structures and Algorithms with Python book, or if you have suggestions for improvements, then please [raise an issue in this repository]([https://github.com/PacktPublishing/JavaScript-from-Beginner-to-Professional/issues](https://github.com/PacktPublishing/Hands-On-Data-Structures-and-Algorithms-with-Python-Third-Edition/issues)), or email to us.

## Chapter 13, Page 403 - Fixing the reference to `ord` array

There should be a reference calling to the `ord` array as `ord_text` in the `generate_hash` function.

Incorrect code is:
```
else:
    hash_text[i] = ((hash_text[i-1] - ord_text[i-1]) + ord[i+len_pattern-1]) # calculating next hash value using previous value
```
Correct code is:
```
else:
    hash_text[i] = ((hash_text[i-1] - ord_text[i-1]) + ord_text[i+len_pattern-1]) # calculating next hash value using previous value
```

## Chapter 3, Page 61 - Fixed the missing '/' in `binary search` code

There should be `//` in place of `/`

Incorrect code is:
```python
mid = start + (end - start)/2
if arr[mid] == key:  
   return mid
```
Correct code is:
```python
mid = start + (end - start)//2
if arr[mid] == key:  
   return mid
```


## Chapter 1, Page 23 - Fixed the missing outputs

This is the actual dictionary
`mydict = {'a': 1, 'b': 2, 'c': 3}`

|Function |Description |Example|
| :-------:|  :-------: | :-------: | 
| `mydict.pop()`| If a given key is present in the dictionary, then this function will remove the key and return the associated value.   | `print(mydict.pop('b'))` should give you output `2` |
|              `|    | `print(mydict)` should give you output `{'a': 1, 'c': 3}` |
| `mydict.popitem()`|  This method removes the last key-value pair added in the dictionary and returns it as a tuple.  | `print(mydict.popitem())` should give you output `('c', 3)` |
|              `|    | `print(mydict)` should give you output `{'a': 1, 'b': 2}` |
| `mydict.update(<obj>)`| Merges one dictionary with another. Firstly, it checks whether a key of the second dictionary is present in the fi rst dictionary; the corresponding value is then updated. If the key is not present in the fi rst dictionary, then the key-value pair is added.   | It has two dictionaries as `d1 = {'a': 10, 'b': 20, 'c': 30}` and `d2 = {'b': 200, 'd': 400}`|
|                       |    | `d1.update(d2)` should update values of `d2` on `d1` |
|                       |    | `print(d1)` should give you `{'a': 10, 'b': 200, 'c': 30, 'd': 400}` |

