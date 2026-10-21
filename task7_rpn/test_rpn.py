import unittest

from rpn import ERROR, evaluate


class TestRpn(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(evaluate("2 3 +"), 5)
        self.assertEqual(evaluate("5 2 -"), 3)
        self.assertEqual(evaluate("4 5 *"), 20)
        self.assertEqual(evaluate("7 2 /"), 3.5)
        self.assertEqual(evaluate("8 2 /"), 4)

    def test_long(self):
        # (5 + 1) * 2 - 4 / 2 = 10
        self.assertEqual(evaluate("5 1 + 2 * 4 2 / -"), 10)
        self.assertEqual(evaluate("7 8 + 3 2 + /"), 3)

    def test_negative_and_float(self):
        self.assertEqual(evaluate("-3 2 *"), -6)
        self.assertEqual(evaluate("1.5 2 *"), 3)

    def test_one_number(self):
        self.assertEqual(evaluate("42"), 42)

    def test_not_enough(self):
        self.assertEqual(evaluate("2 +"), ERROR)
        self.assertEqual(evaluate("+"), ERROR)

    def test_extra_numbers(self):
        self.assertEqual(evaluate("1 2 3 +"), ERROR)

    def test_zero_division(self):
        self.assertEqual(evaluate("5 0 /"), ERROR)

    def test_unknown(self):
        self.assertEqual(evaluate("2 3 ^"), ERROR)
        self.assertEqual(evaluate("2 x +"), ERROR)

    def test_empty(self):
        self.assertEqual(evaluate(""), ERROR)


if __name__ == "__main__":
    unittest.main(verbosity=2)
