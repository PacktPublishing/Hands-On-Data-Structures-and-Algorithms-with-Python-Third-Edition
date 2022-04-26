def fib(n):
  if n <= 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)

for i in range(5):
  print(fib(i)) 
