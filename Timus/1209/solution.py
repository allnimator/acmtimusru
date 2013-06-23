import math
n = int(raw_input())
s = ""
while n > 0:
	k = int(raw_input())
	res = 0.5 * (1 + math.sqrt(8*k - 7))
	if int(res) == res:
		s += "1 "
	else:
		s += "0 "
	n -= 1
print s