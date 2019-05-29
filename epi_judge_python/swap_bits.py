from test_framework import generic_test


def swap_bits(x, i, j):

    # b = list(bin(x)[2:])
    # mx = max(i,j)+1
    # if mx > len(b):
    #     b=['0']*(mx-len(b)) + b
    # b[-i-1],b[-j-1] = b[-j-1],b[-i-1]
    # ret = int('0b'+''.join(b), 2)
    # return ret

    if (x>>i) &1 != (x>>j) &1: #if not the same
        mask = 1<<i|1<<j
        x^=mask #flip their values!
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("swap_bits.py", 'swap_bits.tsv',
                                       swap_bits))
