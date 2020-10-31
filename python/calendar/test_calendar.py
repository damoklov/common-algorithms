import unittest
from calendar import Calendar, Node


class TestCalendar(unittest.TestCase):

    def setUp(self) -> None:
        self.calendar = Calendar()
        self.calendar_corner_case = Calendar()
        self.test_list = [(0, 1), (3, 5), (4, 8), (5, 8), (9, 12), (10, 12)]
        self.test_list_corner_case = [(0, 1), (3, 5), (4, 8), (4, 10), (5, 8), (9, 12), (10, 12)]
        self.optimized_list = [(0, 1), (3, 8), (9, 12)]
        self.optimized_list_corner_case = [(0, 1), (3, 12)]
        for item in self.test_list:
            self.calendar.insert_into_sorted(Node(item))
        for item in self.test_list_corner_case:
            self.calendar_corner_case.insert_into_sorted(Node(item))

    def tearDown(self) -> None:
        self.calendar = None
        self.calendar_corner_case = None

    def test_insert_into_sorted(self) -> None:
        """
        (0, 1) -> (3, 5) -> (4, 8) -> (5, 8) -> (9, 12) -> (10, 12)
        """
        current = self.calendar.head
        position = 0
        while current.next is not None:
            self.assertEqual(current.data, self.test_list[position],
                             "Failed at %d" % position)
            position += 1
            current = current.next

    def test_insert_into_sorted_corner_case(self) -> None:
        """
        (0, 1) -> (3, 5) -> (4, 8) -> (4, 10) -> (5, 8) -> (9, 12) -> (10, 12)
        """
        current = self.calendar_corner_case.head
        position = 0
        while current.next is not None:
            self.assertEqual(current.data, self.test_list_corner_case[position],
                             "Failed at %d" % position)
            position += 1
            current = current.next

    def test_optimize(self) -> None:
        """
        (0, 1) -> (3, 5) -> (4, 8) -> (5, 8) -> (9, 12) -> (10, 12)
        (0, 1) -> (3, 8) -> (9, 12)
        """
        self.calendar.optimize()
        current = self.calendar.head
        position = 0
        while current.next is not None:
            self.assertEqual(current.data, self.optimized_list[position],
                             "Failed at %d" % position)
            position += 1
            current = current.next

    def test_optimize_corner_case(self) -> None:
        """
        (0, 1) -> (3, 5) -> (4, 8) -> (4, 10) -> (5, 8) -> (9, 12) -> (10, 12)
        (0, 1) -> (3, 12)
        """
        self.calendar_corner_case.optimize()
        current = self.calendar_corner_case.head
        position = 0
        while current.next is not None:
            self.assertEqual(current.data, self.optimized_list_corner_case[position],
                             "Failed at %d" % position)
            position += 1
            current = current.next


if __name__ == '__main__':
    unittest.main()
