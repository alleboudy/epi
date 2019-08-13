from test_framework import generic_test


def search_smallest(A):
    left,right = 0, len(A)-1

    while left<right:
        mid = left + (right-left)//2
        if A[mid]>A[right]:
            left  =mid+1
        else:
            right = mid

    return right


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
