from test_framework import generic_test
import collections

def can_form_palindrome(s):
    #d = collections.Counter(list(s))
    #oddCtr = 0
    #isPal=True
    #for v in d.values():
    #    if v%2!=0:
    #        oddCtr+=1
    #        if oddCtr>1:
    #            isPal=False
    #            break
    #return isPal

    return sum(v%2 for v in collections.Counter(s).values())<=1
            

    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
