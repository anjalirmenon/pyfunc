def combine (a,b):
	return 0, a[1] + b[1]

total = reduce(combine, items)[1]
