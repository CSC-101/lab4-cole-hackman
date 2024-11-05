import data
import lab4
import unittest
from lab4 import Point

from lab4 import x_coordinates


# Write your test cases for each part below.

class TestCases(unittest.TestCase):

    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_first_element_2(self):
        input = [[], [9,7], [6,5]]
        result = lab4.first_element(input)
        expected = [9, 6]
        self.assertEqual(expected, result)

    # Part 2
    def test_x_coordinates_1(self):
        input = []
        result = lab4.x_coordinates(input)
        expected = []
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        input = [Point(5.0,9.0), Point(-4.0, 1.0)]
        result = lab4.x_coordinates(input)
        expected = [5.0, -4.0]
        self.assertEqual(expected, result)

    # Part 3
    def test_are_in_positive_quadrant_1(self):
        input = [Point(-5.0, -6.0), Point(2.0,2.0), Point(-4.0, 6.0)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [Point(2.0, 2.0)]
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_2(self):
        input = [Point(1.0, -3.0), Point(6.0,4.0), Point(1.0, 9.0)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [Point(6.0, 4.0), Point(1.0, 9.0)]
        self.assertEqual(expected, result)


    # Part 4
    def test_distance_1(self):
        result = lab4.distance(Point(0.0,0.0), Point(5.0,0.0))
        expected = 5.0
        self.assertEqual(expected, result)

    def test_distance_2(self):
        result = lab4.distance(Point(1.0,2.0), Point(4.0,6.0))
        expected = 5.0
        self.assertEqual(expected, result)


    # Part 5
    def test_manhattan_distance_1(self):
        result = lab4.manhattan_distance(Point(0.0,0.0), Point(5.0,0.0))
        expected = 5.0
        self.assertEqual(expected, result)

    def test_manhattan_distance_2(self):
        result = lab4.manhattan_distance(Point(1.0,2.0), Point(4.0,6.0))
        expected = 7.0
        self.assertEqual(expected, result)


    # Part 6
    def test_distanceall_1(self):
        input = [Point(3, 4), Point(0,0)]
        result = lab4.distance_all(input)
        expected = [7, 0]
        self.assertEqual(expected, result)

    def test_distanceall_2(self):
        input = [Point(6, 1), Point(9,0), Point(4, 2)]
        result = lab4.distance_all(input)
        expected = [7, 9, 6]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
