def init_func(self, name):
    self.name = name


def say_name_func(self):
    print(self.name)


def send_message_func (self, message):
    self.message = message
    print(self.message)


Bot = type(
    'type_parent_class',
    (),
    {
        '__init__': init_func,
        'say_name': say_name_func,
        'send_message': send_message_func,
    }
)

#my_class = Bot('Roman')
#my_class.say_name()
#my_class.send_message('Hello')


def second_init_func(self, name, url=None, chat_id=None):
    self.url = url
    self.chat_id = chat_id
    self.name = name


def set_url_func(self, url):
    self.url = url


def set_chat_id_func(self, chat_id):
    self.chat_id = chat_id


def second_send_message_func(self, message):
    self.message = message
    print(f'TelegramBot says: {self.message} \nChat_id: {self.chat_id} \nUrl: {self.url}')


Telegram_Bot = type(
    'telegram_bot',
    (Bot,),
    {
        '__init__': second_init_func,
        'say_name': say_name_func,
        'set_chat_id': set_chat_id_func,
        'set_url': set_url_func,
        'send_message': second_send_message_func,
    }
)

TG = Telegram_Bot('Roman')
TG.say_name()
TG.send_message('Hello')
TG.set_url('some url')
TG.set_chat_id('some id')
TG.send_message('Hello')

