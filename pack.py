def pack(seq):
	result = []
	temp = []	
	last = None
	for current in seq:
		if current == last:
			temp.append(current)
		else:
			result.append(temp)
			temp = [current]
			last = current
			result.append(temp)
	return result	


