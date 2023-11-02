from game import Game
from board import Board
from gameController import GameController

WIDTH = 480
HEIGHT = 480
SCALE = 60
b = Board(WIDTH,HEIGHT,SCALE)
g = Game(b)
controller = GameController(g)
print("next player: You, color:{}".format("black"))

def setup():
    size(480, 480);
    controller.game.board.display()
    make_starter_move()

def draw():
    pass
def no_more_moves():
    temp = g.moves_left
    for item in temp:
        [x,y] = g.get_position_X_Y(item)
        if(g.is_valid_move(g.player_black, x, y)):
            return False
    return True

def mouseClicked():
    x = mouseY // b.screen_scale
    y = mouseX // b.screen_scale
    # player move
    if controller.make_move(x,y,True) is True:
        temp = g.moves_left
        for item in temp:
            [x,y] = g.get_position_X_Y(item)
            pc_result = controller.make_move(x,y,True)
            if pc_result is True:
                print("Your turn")
                if(no_more_moves()):
                    g.get_winner()
                    exit(0)
                break
        if len(temp) == 0:
            if g.white_count> g.black_count:
                print("computer win")
            else:
                print("you win")
            exit(0)
    else:
        print("invalid move, your turn")


def make_starter_move():
    for i in range(2):
        x = HEIGHT//SCALE//2-1
        y = WIDTH//SCALE//2-1+i
        controller.make_move(x,y,False)
    for i in range(2):
        x = HEIGHT//SCALE//2
        y = WIDTH//SCALE//2-i
        controller.make_move(x,y,False)
