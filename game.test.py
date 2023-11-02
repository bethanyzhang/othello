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

    assert g.steps_remaining == 63
    assert g.white_count == 0
    assert g.black_count == 0
    assert g.get_winner() == "It's a Tie game"
    assert g.player_black.name == "unknown_player"
    assert g.player_white.name == "computer"
    assert g.current_player.name == "unknown_player"
    assert g.current_player.name == "unknown_player"
    assert len(g.index_position) == 8
    assert len(g.index_position[0]) == 8
    assert g.first_move is True
    assert len(g.moves_left) == 64


def test_get_up():
    x = 1
    y = 1
    assert g.get_up(x, y) == [0, 1]


def test_get_left():
    [x, y] = [12, 3]
    assert g.get_left(x, y) == [12, 2]


def test_get_right():
    [x, y] = [12, 3]
    assert g.get_right(x, y) == [12, 4]


def test_get_down():
    [x, y] = [12, 2]
    assert g.get_down(x, y) == [7, 2]  # cant pass row 7
    assert g.get_down(1, 2) == [2, 2]


def test_get_index():

    [x, y] = [0, 1]
    assert g.get_index(x, y) == 1
    [x, y] = [2, 2]
    assert g.get_index(x, y) == 18


def test_get_winner():
    g.white_count = 12
    g.black_count = 12
    assert g.get_winner() == "It's a Tie game"
    g.white_count += 1
    assert g.get_winner() == "winner is white"
    g.black_count += 2
    assert g.get_winner() == "winner is black"


def test_is_valid_move():

    assert g.is_valid_move(g.player_white, 3, 2) is False
    g.tiles[25].color = 'black'
    assert g.is_valid_move(g.player_white, 3, 2) is True
    assert g.is_valid_move(g.player_white, 3, 0) is True


test_constructor()
test_get_up()
test_get_left()
test_get_right()
test_get_down()
test_get_index()
test_get_winner()
test_is_valid_move()
