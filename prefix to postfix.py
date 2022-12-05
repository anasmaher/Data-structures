s = "*-A/BC-/AKL"
stack = []

operators = set(['+', '-', '*', '/', '^'])
s = s[::-1]
for i in s:
	if i in operators:
		a = stack.pop()
		b = stack.pop()
		temp = a+b+i
		stack.append(temp)
	else:
		stack.append(i)
print(*stack)
