def isOperator(x):

	if x == "+":
		return True

	if x == "-":
		return True

	if x == "/":
		return True

	if x == "*":
		return True

	return False


def postToPre(post_exp):

	s = []
	length = len(post_exp)
	for i in range(length):
		if (isOperator(post_exp[i])):
			op1 = s[-1]
			s.pop()
			op2 = s[-1]
			s.pop()
			temp = post_exp[i] + op2 + op1
			s.append(temp)
		else:
			s.append(post_exp[i])

	
	ans = ""
	for i in s:
		ans += i
	return ans
