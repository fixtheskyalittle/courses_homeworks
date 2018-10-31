import random

number_user = int(input (" Enter the number: "))
random_number = random.randint(0,number_user)
number_user2 = int(input(" Enter the number: "))
random_number2 = random.sample(range(random_number), number_user2)
print(random_number, random_number2)