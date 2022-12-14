phone_list = {}
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
        if phone_nr.isdigit():
            phone_list[name] = phone_nr
            print(f'The name {name} added')
        else:
            print('Only number required, please try again')

    elif 'delete ' in command:
        del_name = command.split()[1]
        if del_name[0] == '<' and del_name[-1] == '>':
            name = del_name
            if del_name[1:-1] not in phone_list:
                print('This name is not in list, try another one')
            else:
                phone_list.pop(del_name[1:-1])
                print(f'Name "{del_name[1:-1]}" is deleted')
        else:
            print('Please use "<" and ">" around the name like it was shown.')

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