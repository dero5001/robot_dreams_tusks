import re


file_name = input('Please enter the file name that you want to encode: ')

try:
    with open(file_name, 'r') as file:
        data = file.read()

except FileNotFoundError:
    print('There is no such file, try another one')

else:
    encoded_data = re.sub('\S+@\S+', '*@*', data)
    with open(file_name, 'w+') as file:
        file.write(encoded_data)
    print('Done')
