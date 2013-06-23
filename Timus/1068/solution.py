an = int(raw_input())
n = an
if an < 1:
	n = abs(an) + 2	
print "%s" %(n * (1 + an) / 2)