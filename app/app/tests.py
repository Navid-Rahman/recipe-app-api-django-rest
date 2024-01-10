"""
Sample test file
"""

from django.test import SimpleTestCase

from app import calc

class ClacTests(SimpleTestCase):
    """ Test the calc module """

    def test_add_numbers(self):
        """ Test the add function """
        # self.assertEqual(calc.add(3, 8), 11)

        result = calc.add(3, 8)

        self.assertEqual(result, 11)


    def test_subtract_numbers(self):
        """ Test the subtract function """
        # self.assertEqual(calc.subtract(5, 11), 6)

        result = calc.subtract(5, 11)

        self.assertEqual(result, 6)