class User:
    def __init__(self, name):
        self.name = name.upper()

    def __eq__(self, other):
        return self.name == other


user_1 = User('romAn')
user_2 = User('rOman')

print(user_1 == user_2)
