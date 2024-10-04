class PosBox:
    x1: int
    y1: int
    x2: int
    y2: int

    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Position:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, deltaX: int, deltaY: int):
        self.x += deltaX
        self.y += deltaY

    def limit(self, box: PosBox):
        if self.x < box.x1:
            self.x = box.x1
        if self.y < box.y1:
            self.y = box.y1
        if self.x > box.x2:
            self.x = box.x2
        if self.y > box.y2:
            self.y = box.y2

    def to_tuple(self):
        return (self.x, self.y)
