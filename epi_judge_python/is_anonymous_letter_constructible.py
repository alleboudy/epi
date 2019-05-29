from test_framework import generic_test
import collections

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    mag = collections.Counter(magazine_text)
    lett = collections.Counter(letter_text)
    is_con = True
    for k in lett.keys():
        if not k in mag or mag[k]<lett[k]:
            is_con = False
            break
    return is_con


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
