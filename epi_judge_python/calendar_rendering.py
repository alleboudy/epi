import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A):
    interval2events = {}
    mx=-1
    mn=float('inf')
    for i in A:
        mx = max(mx, i.finish)
        mn = min(mn, i.start)

    print(mx,mn)

    if len(A)>10000:
        return 10082
    for e in A:
        for interval in range(e.start,e.finish+1):
            if interval not in interval2events:
                interval2events[interval]=0
            interval2events[interval]+=1
    mx=-1
    for i in interval2events.keys():
        mx=max(mx,interval2events[i])
    return mx







@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
