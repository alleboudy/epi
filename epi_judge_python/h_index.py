from test_framework import generic_test


def h_index(citations):
    # TODO - you fill in here.

    citations.sort()

    n = len(citations)

    for i in range(n):
        if citations[i]>= n-i:
            return n -i

    return 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main("h_index.py", 'h_index.tsv', h_index))
