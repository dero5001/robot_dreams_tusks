import re


file_name = input('Please enter the file name that you want to encode: ')

try:
    with open(file_name, 'r') as file:
        incoming_data = file.read()

except NameError:
    print('There is no such file, try another one')

else:
    find_list = re.findall('\S+@\S+', incoming_data)
    find_list.reverse()
    cycle = len(find_list)

    for item in find_list:
        incoming_data = re.sub('\S+@\S+', f'{item[0]}***@***{item[-1]}', incoming_data, cycle)
        cycle -= 1

    with open(file_name, 'w') as file:
        file.write(incoming_data)

    print('Done!')
