import unittest
from writer.paper import Paper
from writer.pencil import Pencil

class TestPaper(unittest.TestCase):

    def test_when_text_is_written_it_is_added_to_paper(self):
        paper = Paper()
        new_text = "I love to write"
        paper.write(new_text)
        self.assertEqual(new_text, paper.text)

    def test_when_text_is_appended_it_is_added_to_end_of_paper(self):
        paper = Paper()
        first_text = "I love to write"
        paper.write(first_text)
        second_text = " but sometimes it makes my hand hurt"
        paper.write(second_text)
        self.assertEqual(paper.text, first_text + second_text)

class TestPencil(unittest.TestCase):

    def test_when_pencil_is_created_it_has_an_initial_point_durability(self):
        initial_point_durability = 100
        pencil = Pencil(initial_point_durability)
        self.assertEqual(initial_point_durability, pencil.point_durability)

if __name__ == "__main__":
    unittest.main()
        