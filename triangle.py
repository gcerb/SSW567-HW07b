# -*- coding: utf-8 -*-
"""
Updated Oct 2025
Updated classifyTriangle()

@author: Gianna Cerbone
"""
def classifyTriangle(a, b, c):
    # Validate input
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # Check triangle inequality
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # Check for equilateral
    if a == b == c:
        return 'Equilateral'

    # Check for right triangle
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return 'Right'

    # Check for isosceles
    if a == b or b == c or a == c:
        return 'Isoceles'

    # Otherwise, scalene
    return 'Scalene'
