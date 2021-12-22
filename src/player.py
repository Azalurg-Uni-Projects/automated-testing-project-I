class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def change_name(self, new_name):
        self.name = new_name
        return self.name

