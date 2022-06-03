def factorial(n):  
    # test for a base case       
    if  n == 0:  
        return 1  
    else:  
        return n*factorial(n-1)    # Do the calculation and a recursive call 
   

 
print(factorial(4))
