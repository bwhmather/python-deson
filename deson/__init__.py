import sys
import numbers
import math
import re


_unset = object()


def parse_int(
    value=_unset, *, max_value=None, min_value=None, required=True
):
    if max_value is not None and min_value is not None:
        assert max_value >= min_value

    def parse(value):
        if value is None:
            if required:
                raise TypeError()
            else:
                return None

        if not isinstance(value, numbers.Real):
            raise TypeError()

        if abs(value) >= 2 ** sys.float_info.mant_dig:
            raise ValueError()

        fractional, integer = math.modf(value)
        if fractional != 0:
            raise ValueError()

        integer = int(integer)

        if max_value is not None and integer > max_value:
            raise ValueError()

        if min_value is not None and integer < min_value:
            raise ValueError()

        return integer

    if value is not _unset:
        return parse(value)
    else:
        return parse


def parse_float(
    value=_unset, *, max_value=None, min_value=None, required=True
):
    if max_value is not None and min_value is not None:
        assert max_value >= min_value

    def parse(value):
        if value is None:
            if required:
                raise TypeError()
            else:
                return None

        if not isinstance(value, numbers.Real):
            raise TypeError()

        if max_value is not None and value > max_value:
            raise ValueError()

        if min_value is not None and value < min_value:
            raise ValueError()

        return float(value)

    if value is not _unset:
        return parse(value)
    else:
        return parse


def parse_text(
    value=_unset, *, max_len=None, min_len=None, pattern=None, required=True
):
    if max_len is not None and min_len is not None:
        assert max_len >= min_len

    if pattern is not None and isinstance(pattern, str):
        pattern = re.compile(pattern)

    def parse(value):
        if value is None:
            if required:
                raise TypeError()
            else:
                return None

        if not isinstance(value, str):
            raise TypeError()

        if max_len is not None and len(value) > max_len:
            raise ValueError()

        if min_len is not None and len(value) < min_len:
            raise ValueError()

        if pattern and pattern.fullmatch(value) is None:
            raise ValueError()

        return value

    if value is not _unset:
        return parse(value)
    else:
        return parse


def parse_set(
    value=_unset, *,
    parse_item=lambda item: item,
    max_len=None, min_len=None,
    allow_duplicates=False,
    required=True
):
    if max_len is not None and min_len is not None:
        assert max_len >= min_len

    def parse(value):
        if value is None:
            if required:
                raise TypeError()
            else:
                return None

        if not isinstance(value, list):
            raise TypeError()

        result = {
            parse_item(item) for item in value
        }

        if not allow_duplicates and len(result) < len(value):
            raise ValueError()

        if max_len is not None and len(result) > max_len:
            raise ValueError()

        if min_len is not None and len(result) < min_len:
            raise ValueError()

        return result

    if value is not _unset:
        return parse(value)
    else:
        return parse


def parse_array(
    value=_unset, *, max_len=None, min_len=None, required=True
):
    raise NotImplementedError()


def parse_dictionary(
    value=_unset, *, schema=None, allow_extra=True, rename=None, required=True
):
    if rename is None:
        def rename_(key):
            return key
    elif isinstance(rename, dict):
        def rename_(key):
            return rename.getdefault(key, key)
    else:
        rename_ = rename

    def parse(value):
        if value is None:
            if required:
                raise TypeError()
            else:
                return None

        if not isinstance(value, dict):
            raise TypeError()

        if not allow_extra and set(value) - set(schema):
            raise ValueError()

        if schema is not None:
            return {
                rename_(key): parser(value.get(key))
                for key, parser in schema.items()
            }
        else:
            return {
                rename_(key): item
                for key, item in value.items()
            }

    if value is not _unset:
        return parse(value)
    else:
        return parse


def parse_bytes(
    value=_unset, *, max_len=None, min_len=None, required=True
):
    raise NotImplementedError()


def parse_datetime(
    value=_unset, *, required=True
):
    raise NotImplementedError()


def parse_uuid(
    value=_unset, *, required=True
):
    raise NotImplementedError()
