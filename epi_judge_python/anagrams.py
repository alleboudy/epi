from test_framework import generic_test, test_utils


def find_anagrams(dictionary):
    result = {}
    for k in dictionary:
        key =''.join( sorted(k))
        if key not in result:
            result[key] = []
        result[key].append(k)

    return [v for k,v in result.items() if len(v)>1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare))
