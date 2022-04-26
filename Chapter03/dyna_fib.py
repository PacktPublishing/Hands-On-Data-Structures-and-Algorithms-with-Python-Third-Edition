def dyna_fib(n, lookup):
    if n == 0:
        return 0
    if n <= 2:
        lookup[n] = 1
    if lookup[n] is None:
        lookup[n] = dyna_fib(n-1, lookup) + dyna_fib(n-2, lookup)
    return lookup[n] 

lookup = [None]*(1000)

for i in range(6): 
    print(dyna_fib(i, lookup)) 
