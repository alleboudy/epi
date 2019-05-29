from test_framework import generic_test


def plus_one(A):
    idx = len(A) -1
    c=1
    while idx>-1:
        A[idx],c = (A[idx]+c,0) if A[idx]+c<=9 else (0,1)
        idx-=1
        if c==0:
            break
    if c==1:
        A.insert(0,1)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
