import unittest

from deson import parse_int, parse_float, parse_text


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

    def test_reject_min(self):
        self.assertRaises(ValueError, parse_int, -1, min_value=0)

    def test_accept_max(self):
        self.assertEqual(parse_int(1, max_value=2), 1)
        self.assertEqual(parse_int(-4, max_value=-4), -4)

    def test_reject_max(self):
        self.assertRaises(ValueError, parse_int, 11, max_value=10)

    def test_reject_imprecise(self):
        self.assertRaises(ValueError, parse_int, 2**53)
        self.assertRaises(ValueError, parse_int, -2**53)

    def test_required(self):
        self.assertRaises(TypeError, parse_int, None)
        self.assertRaises(TypeError, parse_int, None, required=True)
        self.assertEqual(parse_int(None, required=False), None)


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

    def test_required(self):
        self.assertRaises(TypeError, parse_float, None)
        self.assertRaises(TypeError, parse_float, None, required=True)
        self.assertEqual(parse_float(None, required=False), None)


class ParseStringTestCase(unittest.TestCase):
    def test_accept_string(self):
        parsed = parse_text("Hello, World!")

        self.assertEqual(parsed, "Hello, World!")
        self.assertIsInstance(parsed, str)

    def test_reject_non_string(self):
        self.assertRaises(TypeError, parse_text, b"h3110 w0R1d")
        self.assertRaises(TypeError, parse_text, object())
        self.assertRaises(TypeError, parse_text, {})
        self.assertRaises(TypeError, parse_text, [])
        self.assertRaises(TypeError, parse_text, 1.234)
        self.assertRaises(TypeError, parse_text, 11)

    def test_accept_min(self):
        self.assertEqual(parse_text("123456", min_len=5), "123456")
        self.assertEqual(parse_text("12345", min_len=5), "12345")

    def test_reject_min(self):
        self.assertRaises(ValueError, parse_text, "12345", min_len=6)

    def test_accept_max(self):
        self.assertEqual(parse_text("12345", max_len=6), "12345")
        self.assertEqual(parse_text("123456", max_len=6), "123456")

    def test_reject_max(self):
        self.assertRaises(ValueError, parse_text, "12345", max_len=4)

    def test_accept_pattern(self):
        self.assertEqual(parse_text("a----b", pattern=r"a-*b"), "a----b")

    def test_reject_pattern(self):
        self.assertRaises(
            ValueError, parse_text, "begin end", pattern=r"end",
        )
        self.assertRaises(
            ValueError, parse_text, "begin end", pattern=r"begin",
        )

    def test_required(self):
        self.assertRaises(TypeError, parse_text, None)
        self.assertRaises(TypeError, parse_text, None, required=True)
        self.assertEqual(parse_text(None, required=False), None)


loader = unittest.TestLoader()
suite = unittest.TestSuite((
    loader.loadTestsFromTestCase(ParseIntTestCase),
    loader.loadTestsFromTestCase(ParseFloatTestCase),
    loader.loadTestsFromTestCase(ParseStringTestCase),
))
