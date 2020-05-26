class Pencil:
    def __init__(self, point_durability):
        self.point_durability = point_durability

    def write(self, new_text):
        for character in new_text:
            self._write_character(character)

    def _write_character(self, character):
        if character.isupper():
            self.point_durability -= 2
        elif character.islower():
            self.point_durability -= 1        