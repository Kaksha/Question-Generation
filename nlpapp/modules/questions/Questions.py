class Questions:
    def __init__(self, text):
        self.text = text
        if not text == '':
            self.text = self.modify()

    def set_text(self, text):
        self.text = text
        try:
            self.text = self.modify()
        except:
            self.text = ''

    def get_text(self):
        return self.text

    def modify_and_get_text(self, text):
        self.set_text(text)
        return self.text

    def modify(self):
        pass
