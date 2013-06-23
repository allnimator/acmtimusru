n = int(raw_input())
p = []
i = 0
while i < n:
	p.append(map(int, raw_input().split()))
	i += 1
i = 0
s = ''
while i < n:
	j = 0
	while j <= i:
		s += "%d " % p[i - j][j]
		j += 1
	i += 1
j = 1
i -= 1
while j != n:
	c = 0
	while j + c < n:
		s += "%d " % p[i - c][j + c]
		c += 1
	j += 1
print s