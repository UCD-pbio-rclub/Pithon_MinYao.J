#3_3 Use a while loop to print the first 100 prime numbers

import time
import math

count = 0
number = 0


def is_prime(number):
    if number == 1 or number == 0:
        return False
    
    divisor = math.floor(math.sqrt(number))
    for i in range (2,1+divisor):
        if number % i == 0:
            return False
    return True

t0 = time.time()
while count < 100:
    if is_prime(number):
        count += 1
        print (number)
    number += 1
t1 = time.time()
print("Time", t1-t0)

