# Project : create  list with random number

import random
import string

list1 = []
list_length = int(input("Please Enter length of list: "))  # take length of list from user

for i in range(list_length):
    input_element = random.randint(1, list_length) # this line is take random number by randmo.randint
    list1.append(input_element)  # append random number to list1
print(list1)
