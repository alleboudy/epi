from test_framework import generic_test

PRECOMPUTED_PARITY={}


def parity(x):

    # res = 0
    # while x!=0:
    #     res ^=x&1
    #     x>>=1
    # return res


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
