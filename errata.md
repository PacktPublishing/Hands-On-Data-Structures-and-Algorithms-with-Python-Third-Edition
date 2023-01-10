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

## Chapter 3, Page 61 - Fixed the missing '/'

There should be `//` in place of `/`

Incorrect code is:
```
mid = start + (end - start)/2
if arr[mid] == key:  
   return mid
```
Correct code is:
```
mid = start + (end - start)//2
if arr[mid] == key:  
   return mid
```
