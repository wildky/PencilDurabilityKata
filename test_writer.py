import unittest
from writer.paper import Paper
from writer.pencil import Pencil

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
    
    def test_when_write_lower_case_characters_point_durability_decreases_by_one(self):
        new_text = "bird"
        self.pencil.write(new_text, self.paper)
        expected_point_durability = self.max_point_durability - 4*1
        self.assertEqual(self.pencil.point_durability, 
                         expected_point_durability)
   
    def test_when_write_upper_case_characters_point_durability_decreases_by_two(self):
        new_text = "BIRD"
        self.pencil.write(new_text, self.paper)
        expected_point_durability = self.max_point_durability - 4*2
        self.assertEqual(self.pencil.point_durability, 
                         expected_point_durability)

    def test_when_writing_mixed_characters_point_durability_decreases_appropriately(self):
        new_text = "Birds are BEAUTIFUL"
        self.pencil.write(new_text, self.paper)
        expected_point_durability = self.max_point_durability - 10*2 - 7*1
        self.assertEqual(self.pencil.point_durability, 
                         expected_point_durability)
    
    def test_when_writing_spaces_no_effect_on_pencil_durability(self):
        new_text = " "*1000
        self.pencil.write(new_text, self.paper)
        self.assertEqual(self.pencil.point_durability, 
                         self.max_point_durability)

    def test_when_writing_with_insufficient_point_durability_that_nothing_happens(self):
        new_text = "b"*99
        self.pencil.write(new_text, self.paper)
        self.pencil.write("B", self.paper)
        self.assertEqual(self.pencil.point_durability, 1)

    def test_when_attempting_to_write_point_durability_cannot_go_below_0(self):
        new_text = "b"*120
        self.pencil.write(new_text, self.paper)
        self.assertEqual(self.pencil.point_durability, 0)
    
    def test_when_writing_with_pencil_on_paper_it_appears_on_paper(self):
        new_text = "birds are beautiful"
        self.pencil.write(new_text, self.paper)
        self.paper.text = new_text

    def test_when_writing_with_pencil_with_no_durability_space_appears_on_paper(self):
        new_text = "b"*99
        self.pencil.write(new_text, self.paper)
        self.pencil.write("ird", self.paper)
        self.assertTrue(self.paper.text.endswith("bi  "))

    def test_when_sharpen_a_pencil_then_durability_returns_to_initial_value(self):
        self.pencil.write("durability is reduced", self.paper)
        self.assertNotEqual(self.pencil.point_durability, 
                            self.max_point_durability)
        self.pencil.sharpen()
        self.assertEqual(self.pencil.point_durability, 
                         self.max_point_durability)
    
    def test_when_pencil_is_sharpened_then_length_decreases_by_one(self):
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

    def test_when_pencil_erases_then_last_occurence_on_paper_is_replaced_with_spaces(self):
        self.pencil.write("lovely day for a bike ride today", self.paper)
        self.pencil.erase("day", self.paper)
        expected_text = "lovely day for a bike ride to   "
        self.assertEqual(self.paper.text, expected_text)

    def test_when_pencil_erases_twice_then_two_occurence_are_replaced_with_spaces(self):
        self.pencil.write("lovely day for a bike ride today", self.paper)
        self.pencil.erase("day", self.paper)
        self.pencil.erase("day", self.paper)
        expected_text = "lovely     for a bike ride to   "
        self.assertEqual(self.paper.text, expected_text)

    def test_when_erase_and_no_occurence_exists_then_paper_text_is_uneffected(self):
        new_text = "lovely day for a bike ride today"
        self.pencil.write(new_text, self.paper)
        self.pencil.erase("but it is horribly cold so never mind", self.paper)
        self.assertEqual(self.paper.text, new_text)

    def test_when_erase_and_no_occurence_exists_then_pencil_durbaility_is_uneffected(self):
        new_text = "lovely day for a bike ride today"
        self.pencil.write(new_text, self.paper)
        self.pencil.erase("but it is horribly cold so never mind", self.paper)
        self.assertEqual(self.pencil.eraser_durability, 
                         self.initial_eraser_durability)  

    def test_when_erase_a_non_whitespace_character_then_durability_decreases(self):
        self.pencil.write("Erase me, my sweet erasable you", self.paper)
        erased_text = "erasable"
        self.pencil.erase(erased_text, self.paper)
        expected_eraser_durability = (self.initial_eraser_durability 
                                      - len(erased_text))
        self.assertEqual(self.pencil.eraser_durability, 
                         expected_eraser_durability)

    def test_when_erase_whitespace_character_then_durability_is_uneffected(self):
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

    def test_when_edit_whitespace_then_new_text_is_replaced(self):
        original_text = "My plants are dying and I am not sure why"
        edited_text = "My plants are happy and I am not sure why"
        self.pencil.write(original_text, self.paper)
        self.pencil.erase("dying", self.paper)
        self.pencil.edit("happy", 14, self.paper)
        self.assertEqual(self.paper.text, edited_text)

    def test_when_edit_non_whitespace_then_collision_character_is_replaced(self):
        original_text = "butterflies"
        edited_text = "@@@@@@flies"
        self.pencil.write(original_text, self.paper)
        self.pencil.edit("pupper", 0, self.paper)
        self.assertEqual(self.paper.text, edited_text)
    
    def test_when_edit_then_point_durability_decreases_accordingly(self):
        original_text = "Butterflies are good"
        self.pencil.write(original_text, self.paper)
        self.pencil.erase("flies are good", self.paper)
        self.pencil.edit("Balls are fine", 6, self.paper)
        expected_durability = self.max_point_durability - 13 - 19
        self.assertEqual(self.pencil.point_durability, expected_durability)

if __name__ == "__main__":
    unittest.main()
        