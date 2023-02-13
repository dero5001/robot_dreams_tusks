import json
import re

print('Phone list program is started.')

commands = ('You can use next commands:'
            '\n  - stats: If you want to see the quantity of records'
            '\n  - add: if you want to add a new record'
            '\n  - delete <name>: if you want to delete a record with name in <>'
            '\n  - list: to see the list of all records'
            '\n  - show <name>: to see the information about the name in <>'
            '\n  - commands: if you want to see tha command list again'
            '\n  - exit: if you want to exit the program')
print(commands)
file_address = 'phone_book.txt'

try:
    with open(file_address, 'r') as file:
        json_data = file.read()
    phone_list = json.loads(json_data)
except FileNotFoundError:
    phone_list = {}

while True:
    command = input('Please enter a command: ').lower()

    if command == 'stats':
        if len(phone_list) == 0:
            print('There is no records for now')
        else:
            print(len(phone_list))

    elif command == 'add':
        name = input('Please enter a name: ')
        if name in phone_list:
            print('This name is already here')
            continue

        phone_nr = input('Please enter a number: ')

        if re.match('\+380[\d]{9}$', phone_nr) or re.match('380[\d]{9}$', phone_nr) or re.match('0[\d]{9}$', phone_nr):
            phone_list[name] = phone_nr
            json_data = json.dumps(phone_list)

            with open(file_address, 'w') as file:
                file.write(json_data)
            print(f'The name {name} added')

        else:
            print('You input incorrect number, please try again')

    elif 'delete' in command:
        del_name = input('Please enter the name that you want to delete ')

        if del_name not in phone_list:
            print('This name is not in list')

        else:
            phone_list.pop(del_name)
            json_data = json.dumps(phone_list)

            with open(file_address, 'w') as file:
                file.write(json_data)

            print(f'Name "{del_name}" has been deleted')


    elif command == 'list':
        if len(phone_list) == 0:
            print('There is no records for now')
        else:
            for record in phone_list:
                print(record)

    elif 'show ' in command:
        show_name = command.split()[1]
        if show_name[0] == '<' and show_name[-1] == '>':
            name = show_name
            if show_name[1:-1] not in phone_list:
                print('This name is not in list, try another one')
            else:
                print(f'The name: {show_name[1:-1]}, phone number: {phone_list[show_name[1:-1]]} ')
        else:
            print('Please use "<" and ">" around the name like it was shown.')

    elif command == 'commands':
        print(commands)

    elif command == 'exit':
        break

    else:
        print('Your command is unknown for me.\nIf you forgot command list just enter "commands"')
