import unittest
from pynative.beginner import number_multiplayer


class TestNumberMultiplayer(unittest.TestCase):

    def test_product_less_than_100(self):
        result = number_multiplayer(10, 20)
        self.assertEqual(result, 200)

    def test_product_equals_1000(self):
        result = number_multiplayer(20, 50)
        self.assertEqual(result, 1000)

    def test_product_greater_than_1000(self):
        result = number_multiplayer(50, 30)
        self.assertEqual(result, 80)

    def test_product_with_negative_numbers(self):
        result = number_multiplayer(-10, 20)
        self.assertEqual(result, -200)


if __name__ == '__main__':
    unittest.main()
