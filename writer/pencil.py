class Pencil:
    """
    A writing utensil that can be used to add and edit text on a paper.

    Parameters
    ----------
    max_point_durability : int
        The point durability of the pencil tip when sharpened. 
        It is assumed that the pencil is sharpened before instantiation.
    
    length : int
        The length of the pencil when it is instantiated.

    eraser_durability : int
        The eraser durability of the pencil when it is instantiated.  

    Attributes
    ----------
    max_point_durability : int
        The point durability of the pencil tip when sharpened. 

    point_durability : int
        The current point durability of the pencil tip.
    
    length : int
        The current length of the pencil.

    eraser_durability : int
        The current eraser durability of the pencil.  
    """

    POINT_DEGRADATION_VALUE_UPPER = 2
    POINT_DEGRADATION_VALUE_LOWER = 1
    LENGTH_DEGRADATION_VALUE = 1
    ERASER_DEGRADATION_VALUE = 1
    NON_ERASABLE_CHARACTERS = [" "]
    EDITABLE_CHARACTERS = [" "]
    COLLISION_CHARACTER = "@"
    DULL_POINT_CHARACTER = " "
    ERASED_CHARACTER = " "

    def __init__(self, max_point_durability, length, eraser_durability):
        self.max_point_durability = max_point_durability
        self.point_durability = max_point_durability
        self.length = length
        self.eraser_durability = eraser_durability
    
    def sharpen(self):
        """ 
        Improves point durability of a dull pencil tip.
        Will restore `point_durability` to `max_point_durability`
        and also reduce the pencil `length`. Once a pencil's `length`
        reaches zero, it can no longer be sharpened.
        """

        if self.length > 0:
            self.point_durability = self.max_point_durability
            self.length -= 1

    def erase(self, erased_text, paper):
        """
        Removes text from a paper.
        
        Will remove the most recent occurence of `erased_text` found in the
        paper.text string. If `erased_text` is not found, no action will be 
        taken. Will reduce the pencil's `eraser_durability` accordingly. 
        When `eraser_durability` reaches zero, text will no longer be deleted. 

        Parameters
        ----------
        erased_text : str
        paper : Paper

        See Also
        --------
        writer.paper.Paper : the Paper class
        -------- 
        """

        try:
            first_character_index = paper.text.rindex(erased_text)
        except ValueError:
            return
        final_character_index = first_character_index + len(erased_text) - 1
        current_character_index = final_character_index
        for character in reversed(erased_text):
            if self.eraser_durability == 0:
                break
            self._erase_character(character, current_character_index, paper)
            current_character_index -= 1

    def _erase_character(self, character, index, paper):
        """
        Removes a single character on a paper provided its location.
        This method should not be used externally, use `Pencil.erase()`
        instead.

        If the `character` is erasable, it will be removed from the `paper`
        and the eraser durability will be reduced accordingly. 

        Parameters
        ----------
        character : str with length of 1
            the character to be removed
        index : int 
            the index location of the character on the `Paper.text` string
        paper : Paper
        """

        if self._erasable(character):
            self._insert_character(self.ERASED_CHARACTER, index, paper)
            self.eraser_durability -= self.ERASER_DEGRADATION_VALUE
    
    def _erasable(self, character):
        """
        Determines if a provided character can be erased.
        All characters are erasable except for those included in the 
        Pencil.NON_ERASABLE_CHARACTERS list
        
        Parameters
        ----------
        character : str with length of 1

        Returns
        -------
        boolean
            Whether or not the `character` can be erased.

        See Also
        --------
        Pencil.NON_ERASABLE_CHARACTERS : list of non-erasable characters
        """

        return False if character in self.NON_ERASABLE_CHARACTERS else True

    def write(self, new_text, paper):
        """
        Appends text to the end of a paper.

        Will append `new_text` to the end of paper.text string. Will reduce 
        the pencil's `point_durability` accordingly. When `point_durability`
        reaches zero, new written text will be replaced with white space
        instead of the desired text. If possible, the pencil can be sharpened
        to restore point_durability.

        Parameters
        ----------
        new_text : str
        paper : Paper

        See Also
        --------
        writer.paper.Paper : the Paper class
        -------- 
        """

        for character in new_text:
            self._write_character(character, paper)

    def _write_character(self, character, paper):
        """
        Appends a single character to paper text.
        This method should not be used externally, use `Pencil.write()`
        instead.

        If the pencil's `point durability is large enough, the `character`
        will be appended to the `paper.text` and point durability will be
        reduced accordingly. 

        Parameters
        ----------
        character : str with length of 1
            the character to be appended
        paper : Paper
        """
    
        durability_reduction = self.calculate_point_durability_cost(character)
        if self.point_durability - durability_reduction >= 0:
            self._insert_character(character, len(paper.text), paper)
            self.point_durability -= durability_reduction
        else:
            self._insert_character(self.DULL_POINT_CHARACTER, 
                                   len(paper.text), 
                                   paper)
    
    def edit(self, new_text, index, paper):
        """
        Edits existing text on a paper.

        Will attempt to add `new_text` to the paper.text string starting at 
        the specified `index` (such that the index of the first character in the
        paper text is 0. If the existing text is a non-whitespace character, 
        then a collision character (@) will be written instead of desired new 
        character.   

        Parameters
        ----------
        new_text : str
        index : int
        paper : Paper

        """
        for character in new_text:
            self._edit_character(character, index, paper)
            index += 1
    
    def _edit_character(self, character, index, paper):
        """
        Edits a single `character` at specifed `index` in the `paper` text.
        This method should not be used externally, use `Pencil.edit()`
        instead.

        Parameters
        ----------
        character : str with length of 1
            the new character to be edited in
        index : int
            the index of the character to be replaced on the paper text
        paper : Paper
        """
        character_to_edit = paper.text[index]
        if self._editable(character_to_edit):
            inserted_character = character
        else:
            inserted_character = self.COLLISION_CHARACTER

        durability_reduction = self.calculate_point_durability_cost(character)
        if self.point_durability - durability_reduction >= 0:
            self._insert_character(inserted_character, index, paper)
            self.point_durability -= durability_reduction

    def _editable(self, character):
        """
        Determines if a provided character can be edited.
        Editable characters are included in the 
        Pencil.EDITABLE_CHARACTERS list
        
        Parameters
        ----------
        character : str with length of 1

        Returns
        -------
        boolean
            Whether or not the `character` can be edited.

        See Also
        --------
        Pencil.EDITABLE_CHARACTERS : list of editable characters
        """

        return True if character in self.EDITABLE_CHARACTERS else False

    def calculate_point_durability_cost(self, character):
        """
        Determines how much writing a character will reduce point durability.

        Upper case characters reduce `point_durability` by value equal to 
        `Pencil.POINT_DEGRADATION_VALUE_UPPER` and lower case characters 
        reduce `point_durability` by value equal to 
        `Pencil.POINT_DEGRADATION_VALUE_LOWER`. All other characters do not 
        reduce point durability of the pencil. 

        Parameters
        ----------
        character : str with length of 1
            the character to be written

        Returns
        -------
        int : point durability to be reduced for writing the character
        """

        if character.isupper():
            return self.POINT_DEGRADATION_VALUE_UPPER
        elif character.islower():
            return self.POINT_DEGRADATION_VALUE_LOWER
        else:
            return 0
            
    def _insert_character(self, character, index, paper):
        """
        Low level function for inserting character at specified index of paper text.
        Used by _write_character and _edit_character functions.

        Parameters
        ----------
        character : str with length of 1
            the new character to be edited in
        index : int
            the index of the character to be replaced on the paper text
        paper : Paper
        """

        paper.text = (paper.text[:index] 
                    + character
                    + paper.text[index + 1:])