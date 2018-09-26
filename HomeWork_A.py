import random

number_user = int(input (" Enter the number: "))
number_sample = int(input (" Enter the sample: "))
print (random.sample ( range(number_sample), random.randint (0, number_user)  ))