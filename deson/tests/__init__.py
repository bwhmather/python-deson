import unittest

from deson import parse_int


class ParseIntTestCase(unittest.TestCase):
    def test_accept_int(self):
        self.assertEqual(parse_int(1), 1)

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
        self.assertRaises(ValueError, parse_int(2**53))
        self.assertRaises(ValueError, parse_int(-2**53))


loader = unittest.TestLoader()
suite = unittest.TestSuite(())
