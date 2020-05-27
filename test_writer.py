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
        self.max_point_durability = 100
        self.initial_length = 10
        self.initial_eraser_durability = 50
        self.pencil = Pencil(self.max_point_durability, 
                             self.initial_length, 
                             self.initial_eraser_durability)
        self.paper = Paper()

    def test_when_pencil_is_created_it_has_an_max_point_durability(self):
        self.assertEqual(self.max_point_durability, 
                         self.pencil.point_durability)
    
    def test_writing_lower_case_characters_reduces_point_durability_by_one(self):
        new_text = "bird"
        self.pencil.write(new_text, self.paper)
        expected_point_durability = self.max_point_durability - 4*1
        self.assertEqual(self.pencil.point_durability, 
                         expected_point_durability)
   
    def test_writing_upper_case_characters_reduces_point_durability_by_two(self):
        new_text = "BIRD"
        self.pencil.write(new_text, self.paper)
        expected_point_durability = self.max_point_durability - 4*2
        self.assertEqual(self.pencil.point_durability, 
                         expected_point_durability)

    def test_writing_upper_and_lower_case_characters(self):
        new_text = "Birds are BEAUTIFUL"
        self.pencil.write(new_text, self.paper)
        expected_point_durability = self.max_point_durability - 10*2 - 7*1
        self.assertEqual(self.pencil.point_durability, 
                         expected_point_durability)
    
    def test_writing_spaces_has_no_effect_on_pencil_durability(self):
        new_text = " "*1000
        self.pencil.write(new_text, self.paper)
        self.assertEqual(self.pencil.point_durability, 
                         self.max_point_durability)

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

    def test_when_sharpen_a_pencil_durability_returns_to_initial_value(self):
        self.pencil.write("durability is reduced", self.paper)
        self.assertNotEqual(self.pencil.point_durability, 
                            self.max_point_durability)
        self.pencil.sharpen()
        self.assertEqual(self.pencil.point_durability, 
                         self.max_point_durability)
    
    def test_when_sharpened_pencil_length_decreases_by_one(self):
        initial_length = self.pencil.length
        self.pencil.sharpen()
        self.assertEqual(initial_length - 1, self.pencil.length)

    def test_when_pencil_length_is_zero_durability_is_not_restored(self):
        for x in range(10):
            self.pencil.sharpen()
            x += 1
        self.pencil.write("shreddin that pencil", self.paper)
        expected_durability = self.pencil.point_durability
        self.pencil.sharpen()
        self.assertEqual(self.pencil.point_durability, expected_durability)

    def test_when_pencil_erases_last_occurence_on_paper_is_replaced_with_spaces(self):
        self.pencil.write("lovely day for a bike ride today", self.paper)
        self.pencil.erase("day", self.paper)
        expected_text = "lovely day for a bike ride to   "
        self.assertEqual(self.paper.text, expected_text)

    def test_when_pencil_erases_twice_two_occurence_are_replaced_with_spaces(self):
        self.pencil.write("lovely day for a bike ride today", self.paper)
        self.pencil.erase("day", self.paper)
        self.pencil.erase("day", self.paper)
        expected_text = "lovely     for a bike ride to   "
        self.assertEqual(self.paper.text, expected_text)

    def test_when_erase_and_no_occurence_exists_paper_text_is_uneffected(self):
        new_text = "lovely day for a bike ride today"
        self.pencil.write(new_text, self.paper)
        self.pencil.erase("but it is horribly cold so never mind", self.paper)
        self.assertEqual(self.paper.text, new_text)

    def test_when_erase_and_no_occurence_exists_pencil_durbaility_is_uneffected(self):
        new_text = "lovely day for a bike ride today"
        self.pencil.write(new_text, self.paper)
        self.pencil.erase("but it is horribly cold so never mind", self.paper)
        self.assertEqual(self.pencil.eraser_durability, 
                         self.initial_eraser_durability)  

    def test_when_erase_a_non_whitespace_character_durability_decreases(self):
        self.pencil.write("Erase me, my sweet erasable you", self.paper)
        erased_text = "erasable"
        self.pencil.erase(erased_text, self.paper)
        expected_eraser_durability = (self.initial_eraser_durability 
                                      - len(erased_text))
        self.assertEqual(self.pencil.eraser_durability, 
                         expected_eraser_durability)

    def test_when_erase_whitespace_character_durability_is_uneffected(self):
        self.pencil.write("Erase me, my sweet erasable you", self.paper)
        erased_text = "Erase me, my "
        self.pencil.erase(erased_text, self.paper)
        expected_eraser_durability = self.initial_eraser_durability - 10
        self.assertEqual(self.pencil.eraser_durability, 
                         expected_eraser_durability)

    def test_when_eraser_durability_reaches_zero_during_erase_session_nothing_else_is_erased(self):
        self.pencil.eraser_durability = 6
        self.pencil.write("I am ready for a quarantine snacky snack", self.paper)
        self.pencil.erase("ky snack", self.paper)
        self.assertEqual(self.paper.text, "I am ready for a quarantine snack       ")

    def test_when_edit_at_specified_location_of_whitespace_text_is_replaced(self):
        original_text = "My plants are dying and I am not sure why"
        edited_text = "My plants are happy and I am not sure why"
        self.pencil.write(original_text, self.paper)
        self.pencil.erase("dying", self.paper)
        self.pencil.edit("happy", 14, self.paper)
        self.assertEqual(self.paper.text, edited_text)

if __name__ == "__main__":
    unittest.main()
        