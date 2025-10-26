import unittest
from triangle import classify_triangle # Import function to be tested

# Class for unit tests with simulated user inputs
class TestTriangles(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(3, 3, 4), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right")
        self.assertEqual(classify_triangle(5, 12, 13), "Scalene Right")

    def test_isosceles_right(self):
        self.assertEqual(classify_triangle(1, 1, 2**0.5), "Isosceles Right")

    def test_not_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Not a triangle")
        self.assertEqual(classify_triangle(10, 1, 1), "Not a triangle")

if __name__ == '__main__':
    unittest.main() # pragma: no cover
