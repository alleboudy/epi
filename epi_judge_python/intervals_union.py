import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals):
    result = []
    intervals.sort(key=lambda x : (x.left.val, not x.left.is_closed,x.right.val,not x.right.is_closed))

    ptr = 0
    
    while ptr<len(intervals):
        min_start = intervals[ptr].left
        max_end = intervals[ptr].right
        ptr+=1
        while ptr<len(intervals) and ( intervals[ptr].right.val<=max_end.val or intervals[ptr].left.val <= max_end.val):
            if max_end.val==intervals[ptr].right.val:
                max_end = intervals[ptr].right if  intervals[ptr].right.is_closed else max_end
            elif max_end.val<intervals[ptr].right.val:
                if not (max_end.val==intervals[ptr].left.val and ( not max_end.is_closed and not intervals[ptr].left.is_closed)):
                    max_end = intervals[ptr].right
                else:
                    break
            ptr+=1

        result.append(Interval(min_start,max_end))
    return result


        


    


    
    


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intervals_union.py",
                                       "intervals_union.tsv",
                                       union_of_intervals_wrapper))
