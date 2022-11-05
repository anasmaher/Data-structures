class Stack:

    def __init__(self):
        self.elements = []
        self.size = 0

    def push(self, value):
        self.elements.append(value)
        self.size += 1

    def pop(self):
        if not self.size:
            return print("Stack is empty")
        self.elements.pop()
        self.size -= 1

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
            return print("Stack is empty")
        for i in range(self.size - 1, -1, -1):
            print(self.elements[i], end=" ")


def toPostfix(exp):
    st = Stack()
    result = []
    mp = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
        '(': 0
    }

    for i in exp:
        if i == '(':
            st.push(i)
        elif i == ')':
            while st.getTop() != '(':
                result.append(st.getTop())
                st.pop()
            st.pop()
        elif i == '+' or i == '-' or i == '/' or i == '*' or i == '^':
            if not st.getSize():
                st.push(i)
            else:
                while st.getSize() and mp[st.getTop()] >= mp[i]:
                    result.append(st.getTop())
                    st.pop()
                st.push(i)
        else:
            result.append(i)

    while st.getSize():
        result.append(st.getTop())
        st.pop()

    return result

#print(toPostfix("(2-3+4)*(5+6*7)"))