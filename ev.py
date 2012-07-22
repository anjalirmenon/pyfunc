import itertools
def is_even(x):
	return (x%2) == 0

itertools.ifilterfalse(is_even,itertools.count(10))
