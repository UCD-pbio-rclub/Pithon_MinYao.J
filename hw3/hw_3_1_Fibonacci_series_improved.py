#Write a for loop that prints the first 100 numbers in the Fibonacci series

import time

Fibo = 1
F1 = 0
F2 = 0

print(Fibo)

t0 = time.time()
for counter in range(1, 100):
    F1 = F2
    F2 = Fibo
    Fibo = F1 + F2
    print(Fibo)
t1 = time.time()
print("Time", t1-t0)