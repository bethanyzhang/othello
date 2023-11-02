class Tile:
    def __init__(self, id, x, y, d):
        self.id = id
        self.x = x
        self.y = y
        self.d = d
        self.color = 'none'
        self.available = True
        self.flip_tile_index = set()

    def display(self, color, flip):
        text(self.id, self.x, self.y+self.d)
        [r, g, b] = [255, 255, 255] if color == "white" else [1, 1, 1]
        if self.available:
            fill(r, g, b)
            stroke(34, 139, 34)
            strokeWeight(3)
            displayOffset = (self.d+10)//2
            ellipse(self.x+displayOffset, self.y+displayOffset, self.d, self.d)
            self.available = False
            self.color = color
        if flip:
            fill(r, g, b)
            stroke(34, 139, 34)
            strokeWeight(3)
            displayOffset = (self.d+10)//2
            ellipse(self.x+displayOffset, self.y+displayOffset, self.d, self.d)
            self.available = False
            self.color = color

    def __repr__(self):
        return "id:{}, x:{}, y:{}, d:{}".format(self.id, self.x, self.y, self.d)
