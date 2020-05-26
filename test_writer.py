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
        self.paper = Paper()

    def test_when_pencil_is_created_it_has_an_initial_point_durability(self):
        self.assertEqual(self.initial_point_durability, self.pencil.point_durability)
    
    def test_writing_lower_case_characters_reduces_point_durability_by_one(self):
        new_text = "bird"
        self.pencil.write(new_text, self.paper)
        expected_point_durability = self.initial_point_durability - 4*1
        self.assertEqual(self.pencil.point_durability, expected_point_durability)
   
    def test_writing_upper_case_characters_reduces_point_durability_by_two(self):
        new_text = "BIRD"
        self.pencil.write(new_text, self.paper)
        expected_point_durability = self.initial_point_durability - 4*2
        self.assertEqual(self.pencil.point_durability, expected_point_durability)

    def test_writing_upper_and_lower_case_characters(self):
        new_text = "Birds are BEAUTIFUL"
        self.pencil.write(new_text, self.paper)
        expected_point_durability = self.initial_point_durability - 10*2 - 7*1
        self.assertEqual(self.pencil.point_durability, expected_point_durability)

    def test_write_upper_case_character_with_pencil_with_one_durability_does_nothing(self):
        new_text = "b"*99
        self.pencil.write(new_text, self.paper)
        self.pencil.write("B", self.paper)
        self.assertEqual(self.pencil.point_durability, 1)

    def test_durability_cannot_go_below_0(self):
        new_text = "b"*120
        self.pencil.write(new_text, self.paper)
        self.assertEqual(self.pencil.point_durability, 0)
    
    def test_writing_with_pencil_writes_on_paper(self):
        new_text = "birds are beautiful"
        self.pencil.write(new_text, self.paper)
        self.paper.text = new_text

    def test_writing_with_pencil_with_no_durability_writes_space_on_paper(self):
        new_text = "b"*99
        self.pencil.write(new_text, self.paper)
        self.pencil.write("ird", self.paper)
        self.assertTrue(self.paper.text.endswith("bi  "))

if __name__ == "__main__":
    unittest.main()
        