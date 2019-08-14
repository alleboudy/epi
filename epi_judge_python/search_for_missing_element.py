import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A):
    
    xor = 0

    for i,v in enumerate(A):
        xor^=i^v

    diff_bit, miss_or_dup = xor & (~(xor-1)),0

    for i,v in enumerate(A):
        if i & diff_bit:
            miss_or_dup^=i
        if v & diff_bit:
            miss_or_dup^=v
    return DuplicateAndMissing(miss_or_dup, miss_or_dup^xor) if miss_or_dup in A else DuplicateAndMissing(miss_or_dup^xor,miss_or_dup)














def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_missing_element.py",
            'find_missing_and_duplicate.tsv',
            find_duplicate_missing,
            res_printer=res_printer))
