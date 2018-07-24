#hw_3_2_dice_optional
total = 0
import random
for x in range(1,101):
    throw_1 = random.randint (1,6)
    throw_2 = random.randint (1,6)
    throw_3 = random.randint (1,6)
    sum_of_throw = throw_1 + throw_2 + throw_3
    #print (sum_of_throw)
    if sum_of_throw % 2 == 0:
        total += 0
    else:
        total += 1
print (total/100)
