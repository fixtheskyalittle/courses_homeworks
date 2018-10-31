import random

passw = ['password0', 'password1', 'password2', 'password3', 'password4', 'password5', 'password6', 'password7', 'password8', 'password9']
logs = {
    'login0': [passw[0], random.randint(1, 10)],
    'login1': [passw[1], random.randint(1, 10)],
    'login2': [passw[2], random.randint(1, 10)],
    'login3': [passw[3], random.randint(1, 10)],
    'login4': [passw[4], random.randint(1, 10)],
    'login5': [passw[5], random.randint(1, 10)],
    'login6': [passw[6], random.randint(1, 10)],
    'login7': [passw[7], random.randint(1, 10)],
    'login8': [passw[8], random.randint(1, 10)],
    'login9': [passw[9], random.randint(1, 10)]
}
login_input = input('login: ')
if login_input in logs:
    print(logs[login_input][1])
else:
    logs.setdefault(login_input)
    print(logs)
