# -*- coding: utf-8 -*-
"""
Updated Oct 2025
Comprehensive unit tests for classifyTriangle()

@author: Gianna Cerbone
"""

import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):

    # --- Valid Triangles ---

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(3,3,3), 'Equilateral')
        self.assertEqual(classifyTriangle(200,200,200), 'Equilateral')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(3,3,4), 'Isoceles')
        self.assertEqual(classifyTriangle(5,4,5), 'Isoceles')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(4,5,6), 'Scalene')
        self.assertEqual(classifyTriangle(10,15,12), 'Scalene')

    def testRightTriangles(self):
        self.assertEqual(classifyTriangle(3,4,5), 'Right')
        self.assertEqual(classifyTriangle(5,12,13), 'Right')
        self.assertEqual(classifyTriangle(8,6,10), 'Right')

    # --- Invalid Inputs ---

    def testInvalidInputs(self):
        self.assertEqual(classifyTriangle(0,1,1), 'InvalidInput')
        self.assertEqual(classifyTriangle(-1,2,2), 'InvalidInput')
        self.assertEqual(classifyTriangle(201,100,100), 'InvalidInput')
        self.assertEqual(classifyTriangle('a',2,2), 'InvalidInput')

    # --- Not a Triangle ---
    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,2,3), 'NotATriangle')
        self.assertEqual(classifyTriangle(10,1,1), 'NotATriangle')
        self.assertEqual(classifyTriangle(5,9,3), 'NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
