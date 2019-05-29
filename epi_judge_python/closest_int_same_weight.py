from test_framework import generic_test


def closest_int_same_bit_count(x):
    b = bin(x)
    for i in range(1,len(b-2)):
        

    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("closest_int_same_weight.py",
                                       "closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))
