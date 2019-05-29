from test_framework import generic_test


def search_first_of_k(A, k):
    lo,hi = 0,len(A)-1
    idx=-1
    if len(A)==0:
        return idx
    while lo<=hi:
        m = lo+ (hi-lo)//2 
        if A[m]==k:
            idx=m
            hi = m-1
        elif A[m]>k:
            hi = m-1
        else:
            lo= m+1
    if A[m] == k:
        idx = m
    return idx


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
