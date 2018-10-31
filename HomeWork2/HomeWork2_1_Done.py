import string
import random

letters_list = []
number_list = []
c = []
z = []
for i in range(10):
    for x in range(random.randint(1, 11)):
        c = (''.join((random.choice(string.ascii_letters))))
    letters_list.append(c)
for y in range(10):
    for n in range(random.randint(1, 11)):
        z = (''.join((random.choice(string.digits))))
    number_list.append(z)

d_list = dict(zip(letters_list, number_list))

print(d_list)