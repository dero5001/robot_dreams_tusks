class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        self.message = message
        print(self.message)


class TelegramBot(Bot):
    def __init__(self, name, url=None, chat_id=None):
        self.url = url
        self.chat_id = chat_id
        super().__init__(name)

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, message):
        self.message = message
        print(f'TelegramBot says: {self.message} \nChat_id: {self.chat_id} \nUrl: {self.url}')


test = TelegramBot('Roman', 'http')
test.send_message('Hello')
test.set_url(1)
test.set_chat_id('ID')
test.send_message('Hello')


