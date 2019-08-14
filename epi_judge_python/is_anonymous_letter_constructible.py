from test_framework import generic_test
import collections

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    #mag = collections.Counter(magazine_text)
    lett = collections.Counter(letter_text)
    is_con = True
    for k in magazine_text:
        if k in lett:
            lett[k]-=1
            if lett[k]==0:
                del lett[k]
                if len(lett)==0:
                    return True

            
    return len(lett)==0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
