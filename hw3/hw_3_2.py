#hw_3_2_dice
total = 0
import random
for x in range(1,101):
    throw = random.randint (1,6)
    #print (throw)
    if throw == 1 or throw == 3 or throw == 5:
        total += 1
    else:
        total += 0
print (total/100)

