from game import Game


class GameController:
    def __init__(self, game):
        self.game = game
        self.current_color = "black"

    def display_board(self):
        self.game.board.display()

    def make_move(self, x, y, started):
        return self.game.make_move(x, y, started)
