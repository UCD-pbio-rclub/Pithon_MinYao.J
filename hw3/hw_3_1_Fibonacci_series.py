#Write a for loop that prints the first 100 numbers in the Fibonacci series

import time

def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-2) + Fibonacci(n-1)     

t0 = time.time()
for x in range(1, 101):
    print(Fibonacci(x))
t1 = time.time()
print("Time", t1-t0)

#Recursion makes it very slow