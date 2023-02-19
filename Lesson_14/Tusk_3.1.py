import re


file_name = input('Please enter the file name that you want to encode: ')

try:
    with open(file_name, 'r') as file:
        incoming_data = file.read()

except NameError:
    print('There is no such file, try another one')

else:
    iteration = re.finditer('\S+@\S+', incoming_data)
    encoded_data = ''

    for item in iteration:
        encoded_data += f'{item.group()[0]}***@***{item.group()[-1]}\n'

    with open(file_name, 'w') as file:
        file.write(encoded_data)
    print('Done')
