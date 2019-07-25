from django.test import TestCase

from app.calc import add, multiply


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test adding 2 numbers"""
        self.assertEqual(add(10, 10), 20)

    def test_multiply_numbers(self):
        """Test multiplying 2 numbers"""
        self.assertEqual(multiply(5, 7), 35)
