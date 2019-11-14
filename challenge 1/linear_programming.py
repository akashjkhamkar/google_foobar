def solution(x):
	result=""
	for i in range(len(x)):
		if ord('a')<=ord(x[i])<=ord('z'):
			result+=chr(ord('a')+ord('z')-ord(x[i]))
		else:
			result+=x[i]
	return result
