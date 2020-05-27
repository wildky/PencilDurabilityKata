class Paper:
    """
    A material that can be written on.

    Attributes
    ----------
    text : str
        The text that is written on the paper.
    """

    def __init__(self):
        self.text = ""

    def write(self, new_text):
        """
        Appends text to end of text existing on the paper.

        Parameters
        ----------
        new_text : str
            The new text that is to be added.
        """
        self.text += new_text