import unittest
from rectangle import Rectangle

class TestInit(unittest.TestCase):
    def test_default(self):
        """Test default constructor values (length=1, width=1)."""
        rect = Rectangle()
        self.assertEqual(rect.length, 1)
        self.assertEqual(rect.width, 1)

    def test_valid_dimensions(self):
        pass  # Does the constructor correctly assign valid length and width?

    def test_negative_length(self):
        pass  # Does it raise a ValueError if length is negative?

    def test_negative_width(self):
        pass  # Does it raise a ValueError if width is negative?

    def test_invalid_type(self):
        pass  # Does it raise a TypeError if input is non-numeric?

class TestArea(unittest.TestCase):
    def test_area(self):
        pass  # Does the area method return correct value (length * width)?

class TestPerimeter(unittest.TestCase):
    def test_perimeter(self):
        pass  # Does the perimeter method return correct value (2 * (length + width))?

class TestStr(unittest.TestCase):
    def test_str_format(self):
        pass  # Does __str__ return a correctly formatted string?

# Think of two additional test methods to further define the behavior of the Rectangle class
class TestAdditional(unittest.TestCase):
    pass

