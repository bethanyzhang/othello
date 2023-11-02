from game import Game
from board import Board
from gameController import GameController

WIDTH = 480
HEIGHT = 480
SCALE = 60
b = Board(WIDTH, HEIGHT, SCALE)
g = Game(b)
controller = GameController(g)


def test_player_constructor():
    p = controller.game.player_white
    assert p.color == 'white'
    assert p.name == 'computer'


test_player_constructor()
