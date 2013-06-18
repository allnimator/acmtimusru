k = int(raw_input())
g = raw_input()
g = map(int, g.split(" "))
g = sorted(g)
res = 0
i = 0
count = k / 2 + 1
while i < count:
	res += g[i] / 2 + 1
	i += 1
print res