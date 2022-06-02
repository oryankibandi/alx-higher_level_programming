#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is".format(number))
str_num = repr(number)
last_num = str_num[-1]
last_num_int = int(last_num)
print(last_num_int)
if last_num_int > 5:
    print("and is greater than 5")
elif last_num_int == 0:
    print("and is 0")
elif last_num_int < 6 and last_num_int != 0:
    print("and is less than 6 and not 0")
