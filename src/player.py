class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def change_name(self, new_name):
        self.name = new_name
        return self.name

    def return_player(self):
        if self.name and self.color:
            return {self.name: self.color}
        else:
            raise ValueError("Something went wrong!")
