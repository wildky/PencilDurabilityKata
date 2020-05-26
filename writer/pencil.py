class Pencil:
    def __init__(self, point_durability):
        self.point_durability = point_durability

    def write(self, new_text):
        self.point_durability -= len(new_text)