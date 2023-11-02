class Board:
    def __init__(self, width, height, screen_scale):
        self.width = width
        self.height = height
        self.screen_scale = screen_scale
        self.col_count = int(self.width/self.screen_scale)
        self.row_count = int(self.height/self.screen_scale)

    def display(self):
        for i in range(self.row_count):
            for j in range(self.col_count):
                x = i * self.screen_scale
                y = j * self.screen_scale
                stroke(0)
                fill(34, 139, 34)
                rect(x, y, self.screen_scale, self.screen_scale)
