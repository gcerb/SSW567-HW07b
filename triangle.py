"""
This module provides functionality to classify triangles 
based on the lengths of their sides.
"""

def classify_triangle(a, b, c):
    """Classify a triangle based on the lengths of its sides."""
    # Sort so largest side is last for right-triangle check
    sides = sorted([a, b, c])
    a, b, c = sides

    # Check for triangle inequality
    if a + b <= c:
        return 'Not a triangle'

    # Classify type of triangle
    if a == b == c:
        triangle_type = 'Equilateral'
    elif a == b or b == c or a == c:
        triangle_type = 'Isosceles'
    else:
        triangle_type = 'Scalene'

    # Check if right triangle Pythagorean theorem)
    if abs(a**2 + b**2 - c**2) < 1e-6:  # floating-point tolerance
        triangle_type += ' Right'

    return triangle_type