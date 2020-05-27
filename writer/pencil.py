class Pencil:

    POINT_DEGADATION_VALUE_UPPER = 2
    POINT_DEGADATION_VALUE_LOWER = 1
    LENGTH_DEGRADATION_VALUE = 1
    ERASER_DEGRADATION_VALUE = 1
    NON_ERASABLE_CHARACTERS = [" "]

    def __init__(self, initial_point_durability, initial_length, eraser_durability):
        self.initial_point_durability = initial_point_durability
        self.point_durability = initial_point_durability
        self.initial_length = initial_length
        self.length = initial_length
        self.eraser_durability = eraser_durability
    
    def sharpen(self):
        if self.length > 0:
            self.point_durability = self.initial_point_durability
            self.length -= 1

    def erase(self, erased_text, paper):
        erase_length = len(erased_text)
        erase_index = paper.text.rfind(erased_text)
        if erase_index != -1:
            character_index = erase_index + erase_length - 1
            for character in erased_text:
                if self.eraser_durability == 0:
                    break
                self._erase_character(character, character_index, paper)
                character_index -= 1

    def _erase_character(self, character, index, paper):
        if self._erasable(character):
            paper.text = (paper.text[:index] 
                          + " "
                          + paper.text[index + 1:])
            self.eraser_durability -= self.ERASER_DEGRADATION_VALUE
    
    def _erasable(self, character):
        return False if character in self.NON_ERASABLE_CHARACTERS else True

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
            return self.POINT_DEGADATION_VALUE_UPPER
        elif character.islower():
            return self.POINT_DEGADATION_VALUE_LOWER
        else:
            return 0