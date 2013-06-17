an = int(raw_input())
d = 1
n = 1
if an < 1:
	d = -1
	n = abs(an) + 2	
else:
	n = an
print "%s" %(n * (1 + an) / 2)