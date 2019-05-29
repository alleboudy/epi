from test_framework import generic_test


def reverse_bits(x):
    b = bin(x)[2:]
    return int('0b'+ (''.join(('0'* (32 - len(b)) +b )[::-1])),2)
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
