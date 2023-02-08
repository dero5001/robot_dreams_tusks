class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        self.message = message
        print(self.message)


test = Bot('Roman')
test.say_name()
test.send_message('Hello')
