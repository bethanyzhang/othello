from game import Game
from board import Board
from gameController import GameController

WIDTH = 480
HEIGHT = 480
SCALE = 60
b = Board(WIDTH, HEIGHT, SCALE)
g = Game(b)
controller = GameController(g)


def test_constructor():
    assert len(controller.game.moves_left) == 64
    assert controller.current_color == "black"


test_constructor()
