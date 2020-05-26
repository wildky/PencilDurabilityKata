class Pencil:
    def __init__(self, initial_point_durability):
        self.initial_point_durability = initial_point_durability
        self.point_durability = initial_point_durability
    
    def sharpen(self):
        self.point_durability = self.initial_point_durability

    def write(self, new_text, paper):
        for character in new_text:
            self._write_character(character, paper)

    def _write_character(self, character, paper):
        durability_reduction = self._calculate_durability_reduction(character)
        if self.point_durability - durability_reduction >= 0:
            paper.write(character)
            self.point_durability -= durability_reduction
        else:
            paper.write(" ")

    def _calculate_durability_reduction(self, character):
        if character.isupper():
            return 2
        elif character.islower():
            return 1 
        else:
            return 0