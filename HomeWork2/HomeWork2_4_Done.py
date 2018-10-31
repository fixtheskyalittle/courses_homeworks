user_input = int(input("Enter the number: "))
for i in range(1, user_input + 1):
  piramid = (" "*(user_input - i) + " *" * i)
  print(piramid)


