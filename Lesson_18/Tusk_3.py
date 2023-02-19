class MyStr(str):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text.upper()


my_str = MyStr('test')
print(my_str)
