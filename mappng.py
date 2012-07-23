def f(s):
  return s.upper()

s=[] 
def my_map(f,s):
  result = []
  for r in s:
	temp = f(r)
	result.append(temp)
  return result
