#3_3 Use a while loop to print the first 100 prime numbers
import time

count = 0
number = 0

def isprime(number):
    result = True
    
    if number == 1 or number == 0:
        result=False
    
    for i in range (2,number):
        if number%i==0:
            result=False
            break
    return result

t0 = time.time()
while count < 100:
    if isprime(number):
        count += 1
        print (number)
    number += 1
t1 = time.time()
print("Time", t1-t0)


