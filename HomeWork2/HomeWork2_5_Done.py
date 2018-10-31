import random
from string import ascii_letters as a_l

random_list = []
a_l = list(a_l)
for i in range(len(a_l)):
    random_list.append(random.randint(0, 51))
random_list.sort()
random_list.reverse()
for j in range(len(a_l)):
    random_list[j] = str(random_list[j]) + a_l[(random_list[j])] + (''.join(random.choice(a_l) for n in range(10)))

print(random_list)