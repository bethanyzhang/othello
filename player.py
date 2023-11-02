

class Player:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.available_moves = set()

    def set_name(self, name):
        self.name = name

    def __repr__(self):
        return "name:{}; color:{}".format(self.name, self.color)
