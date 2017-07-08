import sys
import numbers
import math


def parse_datetime(value):
    raise NotImplementedError()


def parse_int(value, *, max_value=None, min_value=None):
    if not isinstance(value, numbers.Real):
        raise TypeError()

    if abs(value) >= 2 ** sys.float_info.mant_dig:
        raise ValueError()

    fractional, integer = math.modf(value)
    if fractional != 0:
        raise ValueError()

    if max_value is not None and integer > max_value:
        raise ValueError()

    if min_value is not None and integer < min_value:
        raise ValueError()

    return integer


def parse_float(value, *, max_value=None, min_value=None):
    if not isinstance(value, numbers.Real):
        raise TypeError()

    if max_value is not None and value > max_value:
        raise ValueError()

    if min_value is not None and value < min_value:
        raise ValueError()

    return float(value)


def parse_string(value, *, max_len=None, min_len=None, pattern=None):
    raise NotImplementedError()


def parse_bytes(value, *, max_len=None, min_len=None):
    raise NotImplementedError()


def parse_set(value, *, max_len=None, min_len=None):
    raise NotImplementedError()


def parse_array(value, *, max_len=None, min_len=None):
    raise NotImplementedError()


def parse_dictionary(value, *, schema, allow_extra=True):
    raise NotImplementedError()
