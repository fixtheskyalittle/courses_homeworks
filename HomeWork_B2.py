import random

random_number = (random.randint(1000, 1000000))
result = ((random_number % 10000) // 1000)
print("The random number is", random_number, "4 sign", result)