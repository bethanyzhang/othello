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
    assert b.width == 480
    assert b.height == 480
    assert b.screen_scale == 60
    assert b.row_count == 8
    assert b.col_count == 8


test_constructor()
