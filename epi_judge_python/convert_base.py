from test_framework import generic_test
import string

def convert_base(num_as_string, b1, b2):
    
    n=0
    neg=''
    if num_as_string[0]=='-':
        neg = num_as_string[0]
        num_as_string=num_as_string.replace('-','')
    
    for i,d in enumerate(reversed(num_as_string)):
        n+=string.hexdigits.index(d.lower())*b1**i

    result = []

    while n>0:
        d,n =string.hexdigits[n%b2],n//b2
        result.append(d.upper())
       
    

    if len(result)==0:
        return neg+'0'
    return neg+''.join(reversed(result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
