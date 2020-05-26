import unittest
from writer.paper import Paper

class TestPaper(unittest.TestCase):

    def test_when_text_is_written_it_is_added_to_paper(self):
        paper = Paper()
        new_text = "I love to write"
        paper.write(new_text)
        self.assertEqual(new_text, paper.text)

if __name__ == "__main__":
    unittest.main()
        