letters=[chr(ord('a')+i) for i in range(26)]
def solution(x):
	result=""
	for i in range(len(x)-1):
		if x[i] in letters:
			result+=letters[25-letters.index(x[i])]
		else:
			result+=x[i]
	return result
