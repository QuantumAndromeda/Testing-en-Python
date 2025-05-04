class BinaryConverter:
    def convert(self, number, bits):
        raise NotImplemented("Method not implemented")

class Calculator:
    def __init__(self, binary_converter):
        self.binary_converter = binary_converter
        self.result = None

    def my_sum(self, number1, number2):
        self.result = number1 + number2

    def my_subtract(self, number1, number2):
        self.result = number1 - number2

    def my_multiplication(self, number1, number2):
        self.result = number1 * number2

    def my_division(self, number1, number2):
        if number2 == 0:
            raise ValueError("Division by 0 is not legal")
        self.result = number1 / number2

    def is_even(self, number):
        self.result = number % 2 == 0

    def unsigned_int_to_binary(self, number, bits):
        if not isinstance(number, int):
            raise ValueError("Parameter 'number' must be an integer")
        if not isinstance(bits, int):
            raise ValueError("Parameter 'bits' must be an integer")
        if number < 0:
            raise ValueError("Parameter 'number' must be an unsigned integer")
        if number >= 2 ** bits:
            raise  ValueError("Number " + str(number) + " can not be represented with " + str(bits) + " bits")

        self.result = self.binary_converter.convert(number, bits)