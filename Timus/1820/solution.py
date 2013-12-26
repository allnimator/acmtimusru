w = map(int, raw_input().split())
n = w[0]
k = w[1]

if n <= k:
	print 2
else:
	print int((2 * n + k - 1) / k)