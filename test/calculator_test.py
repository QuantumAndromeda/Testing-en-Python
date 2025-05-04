from unittest import TestCase
from unittest.mock import Mock
from parameterized import parameterized
from src.calculator import Calculator


class MyTestCase(TestCase):
    def setUp(self):
        self.assertIsNone(self.calculator.result)

    def tearDown(self):
        self.calculator.result = None
        self.converter.reset_mock()

    @classmethod
    def setUpClass(cls):
        cls.converter = Mock()
        cls.calculator = Calculator(cls.converter)

    @classmethod
    def tearDownClass(cls):
        cls.calculator = None
        cls.converter = None
        print("Calculator and converter removed")

    @parameterized.expand([
        (1, 2, 3),
        (0, 0, 0),
        (-1, -6, -7),
        (-1, 2, 1),
    ])
    def test_my_sum(self, a, b, expected):
        self.calculator.my_sum(a, b)
        self.assertEqual(expected, self.calculator.result, )

    @parameterized.expand([
        (2, 1, 1),
        (0, 0, 0),
        (-1, -6, 5),
        (-1, 2, -3),
    ])
    def test_my_subtract(self, a, b, expected):
        self.calculator.my_subtract(a, b)
        self.assertEqual(expected, self.calculator.result)

    @parameterized.expand([
        (1, 2, 2),
        (10, 0, 0),
        (-1, 3, -3),
        (-1, -2, 2),
    ])
    def test_my_multiplication(self, a, b, expected):
        self.calculator.my_multiplication(a, b)
        self.assertEqual(expected, self.calculator.result)

    @parameterized.expand([
        (1, 2, 0.5),
        (-6, -6, 1),
        (-40, 2, -20),
        (0, 15, 0)
    ])
    def test_my_division(self, a, b, expected):
        self.calculator.my_division(a, b)
        self.assertEqual(expected, self.calculator.result)

    def test_my_division_error(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.my_division(10, 0)
        self.assertEqual("Division by 0 is not legal", str(context.exception))

    @parameterized.expand([
        2,
        10,
        200,
        0
    ])
    def test_is_even_true(self, number):
        self.calculator.is_even(number)
        self.assertTrue(self.calculator.result)

    @parameterized.expand([
        1,
        5,
        387,
        33
    ])
    def test_is_even_false(self, number):
        self.calculator.is_even(number)
        self.assertFalse(self.calculator.result)

    @parameterized.expand([
        (2, 2, "10"),
        (8, 4, "1000"),
        (11, 6, "001011"),
        (33, 8, "00100001"),
    ])
    def test_unsigned_int_to_binary(self, number, bits, expected):
        self.converter.convert.return_value = expected
        self.calculator.unsigned_int_to_binary(number, bits)
        self.assertEqual(expected, self.calculator.result)
        self.converter.convert.assert_called_with(number, bits)
        self.converter.convert.assert_called_once()

    @parameterized.expand([
        ("Number is not int", "3", 1, "Parameter 'number' must be an integer"),
        ("Bits is not int", 2, "1", "Parameter 'bits' must be an integer"),
        ("Number is signed", -2, 1, "Parameter 'number' must be an unsigned integer"),
        ("Not enough bits", 33, 3, "Number 33 can not be represented with 3 bits"),
    ])
    def test_unsigned_int_to_binary_exceptions(self, name, number, bits, expected_msg):
        with self.assertRaises(ValueError) as context:
            self.calculator.unsigned_int_to_binary(number, bits)

        self.assertEqual(expected_msg, str(context.exception))
        self.converter.convert.assert_not_called()
