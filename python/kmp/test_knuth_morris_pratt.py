import main
import unittest


class TestKMP(unittest.TestCase):

    def setUp(self) -> None:
        self.string_1, self.substring_1 = main.read_string('test1.txt')
        self.string_2, self.substring_2 = main.read_string('test2.txt')
        self.string_3, self.substring_3 = main.read_string('test3.txt')

    def tearDown(self) -> None:
        self.string_1, self.substring_1 = None, None
        self.string_2, self.substring_2 = None, None
        self.string_3, self.substring_3 = None, None

    def test_small_string(self):
        result = main.main("test3.txt")
        self.assertEqual(result, [])

    def test_medium_string(self):
        result = main.main("test1.txt")
        self.assertEqual(result, [9, 16, 26])

    def test_long_string(self):
        result = main.main("test2.txt")
        self.assertEqual(result, [9, 16, 53, 64, 193, 200, 246, 305, 315, 333, 340, 350, 368, 375, 385])
