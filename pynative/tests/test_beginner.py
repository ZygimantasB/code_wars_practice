import unittest

from pynative.beginner import number_multiplayer, second_n_value


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


class TestSecondValue(unittest.TestCase):

    def setUp(self):
        self.test_list_even = [1, 2, 3, 4]
        self.test_list_odd = [1, 2, 3, 4, 5]
        self.test_list = [1, 2, 3, 4, 5, 6]

    def test_even_length_list(self):
        result = second_n_value(self.test_list_even)
        self.assertEqual(result, [1, 3])

    def test_odd_length_list(self):
        result = second_n_value(self.test_list_odd)
        self.assertEqual(result, [1, 3, 5])

    def test_element_in_result(self):
        result = second_n_value(self.test_list)
        self.assertIn(1, result)

    def test_element_not_in_result(self):
        result = second_n_value(self.test_list)
        self.assertNotIn([2, 4, 6], result)

    def test_element_result_not_none(self):
        result = second_n_value(self.test_list)
        self.assertIsNotNone(result)

    def test_error_for_non_list_input(self):
        with self.assertRaises(TypeError):
            second_n_value('not a list')


if __name__ == '__main__':
    unittest.main()

