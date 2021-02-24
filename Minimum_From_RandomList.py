# create random list and find minimum number from random list

import random
import string
random_list = []
length_elemet = int(input("Enter length of list: "))  # take length of list from user
for i in range(length_elemet):
    random_list.append(random.randint(1, length_elemet))  # append random number to list
minimum = random_list[0]
for i in range(len(random_list)):
    if random_list[i] < minimum:  # find minimum number from random list
        minimum = random_list[i]
print("The Random List is: ", random_list)
print("Minimum From Random List is: " , minimum)