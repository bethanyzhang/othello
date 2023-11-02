from tile import Tile
from player import Player


class Game:

    def __init__(self, board):
        self.board = board
        self.tiles = self.create_tiles()
        self.steps_remaining = len(self.tiles)-1
        self.white_count = 0
        self.black_count = 0
        self.winner = self.get_winner()
        self.player_black = Player("unknown_player", "black")
        self.player_white = Player("computer", "white")
        self.current_player = self.player_black
        self.index_position = self.create_index_position()
        self.first_move = True
        self.moves_left = [i for i in range(64)]

    def create_tiles(self):
        tiles = []
        scale = self.board.screen_scale
        for i in range(self.board.row_count):
            for j in range(self.board.col_count):
                x = i * self.board.screen_scale
                y = j * self.board.screen_scale
                t = Tile(self.board.col_count*i+j, y, x,
                         scale-10)
                tiles.append(t)
        return tiles

    def create_index_position(self):
        rows, cols = (8, 8)
        array = [[0]*cols]*rows
        return array

    def get_up(self, x, y):
        up = x-1 if x - 1 >= 0 else 0
        return [up, y]

    def get_left(self, x, y):
        left = y-1 if y-1 >= 0 else 0
        return [x, left]

    def get_right(self, x, y):
        right = y+1 if y+1 < self.board.col_count else self.board.col_count - 1
        return [x, right]

    def get_down(self, x, y):
        down = x+1 if x+1 < self.board.row_count else self.board.row_count - 1
        return [down, y]

    def get_index(self, x, y):
        return self.board.col_count*(x) + y

    def get_position_X_Y(self, idx):
        num = idx
        x = num // 8
        y = idx % 8
        return [x, y]

    def get_winner(self):
        return "winner is white" if self.white_count > self.black_count\
            else "winner is black" if self.black_count > self.white_count \
            else "It's a Tie game"

    def is_valid_move(self, player, x, y):
        index = self.get_index(x, y)

        up = self.tiles[index-8 if index-8 >=
                        (index % 8) else index].color == 'none'
        right = self.tiles[index+1 if index+1 <
                           (index // 8)*8 + 8 else index].color == 'none'
        down = self.tiles[index+8 if index + 8 < 64 else index].color == 'none'
        left = self.tiles[index-1 if index-1 >=
                          index//8 else index].color == 'none'
        if (up and right and down and left):
            return False
        up_1 = self.tiles[index-8 if index-8 >=
                          (index % 8) else index].color == player.color
        right_1 = self.tiles[index+1 if index+1 <
                             (index // 8)*8 + 8 else index].color == player.color
        down_1 = self.tiles[index+8 if index + 8 <
                            64 else index].color == player.color
        left_1 = self.tiles[index-1 if index-1 >=
                            index//8 else index].color == player.color

        # check up
        [up, left, right, down] = [False, False, False, False]
        i = index - 8
        temp = []
        while i >= (index % 8):
            if (self.tiles[i].color == 'none'):
                break
            if (up_1 is False and self.tiles[i].color == self.current_player.color):
                for item in temp:
                    self.tiles[item].color = self.current_player.color
                    self.tiles[item].display(self.current_player.color, True)
                    if (self.current_player.color == "white"):
                        self.white_count += 1
                        self.black_count -= 1
                    else:
                        self.white_count -= 1
                        self.black_count += 1

                up = True
                break
            else:
                temp.append(i)
            i -= 8

        # check right
        j = index + 1
        temp = []
        bound_right = (index // 8)*8 + 8
        while j < (bound_right):

            if (self.tiles[j].color == 'none'):
                break
            if (right_1 is False and self.tiles[j].color == self.current_player.color):

                for item in temp:
                    self.tiles[item].color = self.current_player.color
                    self.tiles[item].display(self.current_player.color, True)
                    if (self.current_player.color == "white"):
                        self.white_count += 1
                        self.black_count -= 1
                    else:
                        self.white_count -= 1
                        self.black_count += 1
                right = True
                break
            else:

                temp.append(j)

            j += 1

        # check left
        m = index - 1
        temp = []
        while m >= (index//8):
            if (self.tiles[m].color == 'none'):
                break
            if (left_1 is False and self.tiles[m].color == self.current_player.color):
                for item in temp:

                    self.tiles[item].color = self.current_player.color
                    self.tiles[item].display(self.current_player.color, True)
                    if (self.current_player.color == "white"):
                        self.white_count += 1
                        self.black_count -= 1
                    else:
                        self.white_count -= 1
                        self.black_count += 1
                left = True
                break
            else:
                temp.append(m)

            m -= 1

        # check down
        n = index + 8

        temp = []
        while n <= 56+(index % 8):
            if (self.tiles[n].color == 'none'):
                break
            if (down_1 is False and self.tiles[n].color == self.current_player.color):
                for item in temp:
                    print("down: {}'s color is {}".format(
                        item, self.tiles[item].color))

                    self.tiles[item].color = self.current_player.color
                    self.tiles[item].display(self.current_player.color, True)
                    if (self.current_player.color == "white"):
                        self.white_count += 1
                        self.black_count -= 1
                    else:
                        self.white_count -= 1
                        self.black_count += 1
                down = True
                break
            else:
                temp.append(n)

            n += 8

        return (up or down or left or right)

    def make_move(self, x, y, started):
        if started:
            if (self.is_valid_move(self.current_player, x, y)):
                self.draw_tile(x, y)
                self.current_player = self.player_white \
                    if self.current_player == self.player_black else self.player_black
                return True
            else:
                return False
        else:
            self.draw_tile(x, y)
            self.current_player = self.player_white \
                if self.current_player == self.player_black else self.player_black
            return True

    def draw_tile(self, x, y):
        tile_index = self.board.col_count*(x) + y
        self.moves_left.remove(tile_index)
        if tile_index in self.player_white.available_moves:
            self.player_white.available_moves.remove(tile_index)
        if tile_index in self.player_black.available_moves:
            self.player_black.available_moves.remove(tile_index)
        if (self.steps_remaining == 0):
            print("winner is: {}".format(self.winner))
        if (self.tiles[tile_index].available):
            idx = self.get_index(x, y)
            if idx in self.current_player.available_moves:
                self.current_player.available_moves.remove(idx)
            if self.current_player.color == "white":
                self.tiles[tile_index].display(
                    self.current_player.color, False)
                self.white_count += 1
            else:
                self.tiles[tile_index].display(
                    self.current_player.color, False)
                self.black_count += 1
            self.steps_remaining -= 1
        self.tiles[tile_index].display(
            self.current_player.color, False) if self.current_player.color == "white" \
            else self.tiles[tile_index].display(self.current_player.color, False)
