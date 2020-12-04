# https://www.geeksforgeeks.org/python-make-a-list-of-intervals-with-sequential-numbers/

# Python3 program to Convert list of
# sequential number into intervals
import itertools


def intervals_extract(iterable):

    iterable = sorted(set(iterable))
    for key, group in itertools.groupby(enumerate(iterable),
        lambda t: t[1] - t[0]):
        group = list(group)
        yield [group[0][1], group[-1][1]]


def divide_chunks(list_obj, n):

    for i in range(0, len(list_obj), n):
        yield list_obj[i:i + n] 