# create random list from random string after that find maximum number

import random
import string
random_list = []
length_elemet = int(input("Enter length of list: "))  # take length of list from user

for i in range(length_elemet):
    random_list.append(random.randint(1, length_elemet))  # append random number to list

maximum = random_list[0]
for i in range(len(random_list)):
    if random_list[i] > maximum:  # find maximum number
        maximum = random_list[i]

print("The Random List is: ", random_list)
print("Maximum From Random List is: " , maximum)