import unittest
from writer.paper import Paper

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
        second_text = "but sometimes it makes my hand hurt"
        paper.write(second_text)
        self.assertEqual(paper.text, first_text + second_text)

if __name__ == "__main__":
    unittest.main()
        