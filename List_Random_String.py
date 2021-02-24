# create  list with random string

import random
import string
list1 = []

list_length = int(input("Please Enter length of list: ")) # take length of list from user

for i in range(list_length):
    input_element = random.choice(string.ascii_lowercase + string.ascii_uppercase ) # take random string
    list1.append(input_element)
print(list1)
