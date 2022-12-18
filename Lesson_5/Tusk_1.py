text = input('Please enter some text:')

for symbol in text:
    if symbol.isdigit():
        if (int(symbol) % 2) == 0:
            print(f'The symbol is {symbol}. This is an even number!')
        else:
            print(f'The symbol is {symbol}. This is an odd number!')
    elif symbol.isalnum():
        if symbol.islower():
            print(f'The symbol is {symbol}. This is an small letter!')
        else:
            print(f'The symbol is {symbol}. This is an capital letter!')
    else:
        print(f'Just the symbol {symbol}')
