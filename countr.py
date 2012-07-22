def counter(maximum):
	i = 0
	while i < maximum:
		val = (yield i)
		if val is not None:
			i = val
		else:

			i += 1
try:
	
	it = counter(10)
#for i in range(10):
	print it.next()

	print it.send(8)
	print it.next()
	print it.next()
	print it.next()
finally:
	print "maximum value exceeded"
