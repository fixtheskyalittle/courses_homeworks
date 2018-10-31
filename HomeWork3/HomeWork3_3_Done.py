
user_input = int(input("Enter the end of list: "))
number_list = []

for a in range(1, user_input+1):
    number_list.append(a)

i = 2
z = 3
n = 5
y = 7

while i <= number_list[-1]:
    if 2 + i in number_list:
        number_list.remove(2+i)
    i += 2
while z <= number_list[-1]:
    if 3 + z in number_list:
        number_list.remove(3+z)
    z += 3
while n <= number_list[-1]:
    if 5 + n in number_list:
        number_list.remove(5+n)
    n += 5
while y <= number_list[-1]:
    if 7 + y in number_list:
        number_list.remove(7+y)
    y += 7
print(number_list)

