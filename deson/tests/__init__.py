import unittest

from deson import parse_int, parse_float


class ParseIntTestCase(unittest.TestCase):
    def test_accept_int(self):
        parsed = parse_int(1)

        self.assertEqual(parsed, 1)
        self.assertIsInstance(parsed, int)

    def test_accept_float(self):
        parsed = parse_int(1.0)

        self.assertEqual(parsed, 1)
        self.assertIsInstance(parsed, int)

    def test_reject_fractional(self):
        self.assertRaises(ValueError, parse_int, 1.5)

    def test_reject_non_real(self):
        self.assertRaises(TypeError, parse_int, object())
        self.assertRaises(TypeError, parse_int, {})
        self.assertRaises(TypeError, parse_int, [])
        self.assertRaises(TypeError, parse_int, "1")

    def test_accept_min(self):
        self.assertEqual(parse_int(2, min_value=1), 2)
        self.assertEqual(parse_int(-4, min_value=-4), -4)

    def test_accept_max(self):
        self.assertEqual(parse_int(1, max_value=2), 1)
        self.assertEqual(parse_int(-4, max_value=-4), -4)

    def test_reject_imprecise(self):
        self.assertRaises(ValueError, parse_int, 2**53)
        self.assertRaises(ValueError, parse_int, -2**53)


class ParseFloatTestCase(unittest.TestCase):
    def test_accept_int(self):
        parsed = parse_float(1)

        self.assertEqual(parsed, 1)
        self.assertIsInstance(parsed, float)

    def test_accept_float(self):
        parsed = parse_float(1.0)

        self.assertEqual(parsed, 1.0)
        self.assertIsInstance(parsed, float)

    def test_reject_fractional(self):
        parsed = parse_float(1.5)
        self.assertEqual(parsed, 1.5)
        self.assertIsInstance(parsed, float)

    def test_reject_non_real(self):
        self.assertRaises(TypeError, parse_float, object())
        self.assertRaises(TypeError, parse_float, {})
        self.assertRaises(TypeError, parse_float, [])
        self.assertRaises(TypeError, parse_float, "1")

    def test_accept_min(self):
        self.assertEqual(parse_float(2, min_value=1), 2)
        self.assertEqual(parse_float(-4, min_value=-4), -4)

    def test_reject_min(self):
        self.assertRaises(ValueError, parse_float, 1.99999, min_value=2)

    def test_accept_max(self):
        self.assertEqual(parse_float(1.99999, max_value=2), 1.99999)
        self.assertEqual(parse_float(1.234, max_value=1.234), 1.234)

    def test_reject_max(self):
        self.assertRaises(ValueError, parse_float, 1.000001, max_value=1)


loader = unittest.TestLoader()
suite = unittest.TestSuite((
    loader.loadTestsFromTestCase(ParseIntTestCase),
    loader.loadTestsFromTestCase(ParseFloatTestCase),
))
