import random
from string import ascii_letters as a_l
import os

a_l = a_l.lower()
a_l = list(a_l)
user_input_method = input("Encryption(1) or Decryption(2)? ")
if user_input_method == "1":
    random_number = random.randint(1, 26)
    print(random_number)
    text_for_encrypt = str(input("Enter some text: "))
    text_for_encrypt = text_for_encrypt.lower()
    text_for_encrypt = list(text_for_encrypt)
    for i in range(len(text_for_encrypt)):
        if text_for_encrypt[i] == ' ':
            continue
        else:
            x = text_for_encrypt[i]
            x = a_l.index(x)
            text_for_encrypt[i] = a_l[x + random_number]
    with open('encrypt_text.txt', 'w') as e_t:
        e_t.write(''.join(text_for_encrypt))
        e_t.close()
    print(os.path.abspath('encrypt_text.txt'))
elif user_input_method == "2":
    random_number = int(input('Enter shift: '))
    file_path = input('What a file path: ')
    with open (file_path) as d_f:
        text_for_decrypt = list(d_f.read())
        d_f.close()
    for i in range(len(text_for_decrypt)):
        if text_for_decrypt[i] == ' ':
            continue
        else:
            x = text_for_decrypt[i]
            x = a_l.index(x)
            text_for_decrypt[i] = a_l[x - random_number]
    print(''.join(text_for_decrypt))
else:
    print('Only 1 or 2')