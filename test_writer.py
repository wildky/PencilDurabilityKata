import unittest
from writer.paper import Paper
from writer.pencil import Pencil

class TestPaper(unittest.TestCase):

    def setUp(self):
        self.paper = Paper()
        self.first_text = "I love to write"
        self.second_text = " but sometimes it makes my hand hurt"

    def test_when_text_is_written_it_is_added_to_paper(self):
        self.paper.write(self.first_text)
        self.assertEqual(self.first_text, self.paper.text)

    def test_when_text_is_appended_it_is_added_to_end_of_paper(self):
        self.paper.write(self.first_text)
        self.paper.write(self.second_text)
        self.assertEqual(self.paper.text, self.first_text + self.second_text)


class TestPencil(unittest.TestCase):

    def setUp(self):
        self.initial_point_durability = 100
        self.pencil = Pencil(self.initial_point_durability)

    def test_when_pencil_is_created_it_has_an_initial_point_durability(self):
        self.assertEqual(self.initial_point_durability, self.pencil.point_durability)
    
    def test_writing_lower_case_characters_reduces_point_durability_by_one(self):
        new_text = "bird"
        self.pencil.write(new_text)
        expected_point_durability = self.initial_point_durability - 4*1
        self.assertEqual(self.pencil.point_durability, expected_point_durability)
   
    def test_writing_upper_case_characters_reduces_point_durability_by_two(self):
        new_text = "BIRD"
        self.pencil.write(new_text)
        expected_point_durability = self.initial_point_durability - 4*2
        self.assertEqual(self.pencil.point_durability, expected_point_durability)

    def test_writing_upper_and_lower_case_characters(self):
        new_text = "Birds are BEAUTIFUL"
        self.pencil.write(new_text)
        expected_point_durability = self.initial_point_durability - 10*2 - 7*1
        self.assertEqual(self.pencil.point_durability, expected_point_durability)

if __name__ == "__main__":
    unittest.main()
        