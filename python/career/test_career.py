import unittest
from career import Career


class TestCareer(unittest.TestCase):

    def setUp(self) -> None:
        self.career_1 = Career("graph_1.txt")
        self.career_2 = Career("graph_2.txt")
        self.career_3 = Career("graph_3.txt")
        self.graph = {
            '1': {},
            '2': {'1': 4},
            '3': {'1': 4},
            '4': {'2': 3},
            '5': {'2': 3, '3': 1},
            '6': {'3': 1},
            '7': {'4': 2},
            '8': {'4': 2, '5': 1},
            '9': {'5': 1, '6': 5},
            '10': {'6': 5},
            '11': {'7': 1, '8': 3, '9': 2, '10': 1}
        }

    def tearDown(self) -> None:
        self.career_1 = None
        self.career_2 = None
        self.career_3 = None

    def test_find_optimal_path(self) -> None:
        self.assertEqual(self.career_1.find_optimal_path(), 12, "Not optimal")
        self.assertEqual(self.career_2.find_optimal_path(), 9999, "Not optimal")
        self.assertEqual(self.career_3.find_optimal_path(), 3, "Not optimal")

    def test_reader(self) -> None:
        self.assertEqual(self.career_1.graph, self.graph, "Graph not equal")
