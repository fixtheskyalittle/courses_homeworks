import os

while True:
    user_input = input("Enter path: ")
    if os.path.isfile(user_input):
        user_file = open(user_input)
        user_input_string = user_file.read()
        string_without_spaces = user_input_string.replace(' ', '')
        symbol_dict = {}
        for symbol in string_without_spaces:
            symbol_dict[symbol] = symbol_dict.setdefault(symbol, 0) + 1
        max_symbol = max(symbol_dict, key=symbol_dict.get)
        print(max_symbol)
        user_file.close()
        exit()
    else:
        print("Enter true path: ")
