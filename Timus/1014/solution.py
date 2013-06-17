n = int(raw_input())
result = ""
if n == 0:
	result = "10"
elif n > 0 and n < 10:
	result = "%s" %n
else:
	i = 9
	while n > 9 and i > 1:
		if n % i == 0:
		 n /= i 		 		  
		 result = "%s" %i + result
		 i = 9
 		else:
		 i -= 1
	if n < 10:
		result = "%s" %n + result
	else:
		result = "-1"
print result