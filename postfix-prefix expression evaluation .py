class Stack:
    def __init__(self):
        self.elements = []
        self.size = 0

    def push(self, value):
        self.elements.append(value)
        self.size += 1

    def pop(self):
        if not self.size:
            return "Stack is empty"
        self.size -= 1
        return self.elements.pop()

    def getSize(self):
        return self.size

    def isEmpty(self):
        return not self.size

    def getTop(self):
        if not self.size:
            return "Stack is empty"
        return self.elements[-1]

    def printStack(self):
        if not self.size:
            return "Stack is empty"
        for i in range(self.size-1, -1, -1):
            print(self.elements[i], end=" ")

# postfix-prefix expression evaluation
def evalPostfix(exp):
    stack = Stack()
    for i in exp:
        if i>='0' and i<='9':
            stack.push(i)
        else:
            if stack.getSize() < 2:
                return print("Wrong expression!")
            x=stack.pop()
            y=stack.pop()
            stack.push(str(eval(x+i+y)))

    return float(stack.pop())

def evalPrefix(exp):
    stack = Stack()
    for i in exp[::-1]:
        if i>='0' and i<='9':
            stack.push(i)
        else:
            if stack.getSize() < 2:
                return print("Wrong expression!")
            x=stack.pop()
            y=stack.pop()
            stack.push(str(eval(x+i+y)))

    return float(stack.pop())
