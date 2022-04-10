# https://stackabuse.com/python-how-to-flatten-list-of-lists/
# itertools.chain faster than sum( packed list, [] ) which is [] + elem1 + elem2, ...
# MATLAB syntax is [C{:}]

from itertools import chain

def unpack_and_stack_lists(x):
    # The star unpacks one level
    # chain returns iterator, so need a list cast to rebuild it
    return list(chain(*x))