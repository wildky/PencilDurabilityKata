class Pencil:
    def __init__(self, point_durability):
        self.point_durability = point_durability

    def write(self, new_text):
        for character in new_text:
            self._write_character(character)

    def _write_character(self, character):
        durability_reduction = self._calculate_durability_reduction(character)
        if self.point_durability - durability_reduction >= 0:
           self.point_durability -= durability_reduction
        else:
            pass

    def _calculate_durability_reduction(self, character):
        if character.isupper():
            return 2
        elif character.islower():
            return 1 
        else:
            return 0