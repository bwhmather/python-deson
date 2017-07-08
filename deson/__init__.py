import sys
import numbers
import math


def parse_datetime(value):
    raise NotImplementedError()


def parse_int(value, *, max_value=None, min_value=None):
    raise NotImplementedError()


def parse_float(value, *, max_value=None, min_value=None):
    raise NotImplementedError()


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
