i = 0

while True:
    try:
        user_input = int(input("Vvedi god: "))
    except ValueError:
        i += 1
        if i >= 3:
            print("Mnogo poputok")
            exit()
        print("vvedi 4islo")
        continue
    if user_input % 4 == 0:
        print("Da eto vusokosnui god")
        exit()
    elif user_input % 4 > 2:
        user_input += 1
    elif user_input % 4 == 2:
        user_input += 2
    elif user_input % 4 < 2:
        user_input -= 1
    else:
        print("Sorry polomal")
    print("Blijaiwie vusokosnui god {}".format(user_input))
    exit()

