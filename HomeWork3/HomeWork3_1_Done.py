import random

number_list = []
n = 1

for i in range(random.randint(1, 100)):
    number_list.append(random.randint(1, 100))
print(number_list)
sorted_list = number_list.copy()
while n < len(sorted_list):
    for z in range(len(sorted_list)-1):
        if sorted_list[z] > sorted_list[z+1]:
            sorted_list[z], sorted_list[z+1] = sorted_list[z+1], sorted_list[z]
    n += 1
print(sorted_list)
