class Parser:
    def __init__(self):
        pass

    def parse(self, input_string):
        statement = Statement(input_string)
        pass


class Statement:
    command = None
    arguments = []

    def __init__(self, input_string: str):
        parts = input_string.split(' ')
        self.command = parts[0]
        self.arguments = parts[1:]
        pass
