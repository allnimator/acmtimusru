def diff(idx, current, result, w, s):
	if (idx == n):
		if (abs(2 * current - s) < result):
			result = abs(2 * current - s)
	else:
		result = diff(idx + 1, current, result, w, s)
		result = diff(idx + 1, current + w[idx], result, w, s)
	return result
n = int(raw_input())
w = map(int, raw_input().split())
s = sum(w)
result = diff(0, 0, s, w, s)
print result;