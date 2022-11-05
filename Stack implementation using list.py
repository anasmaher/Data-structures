class Stack: 
    def __init__(self): 
        self.elements = [] 
        self.size = 0

    def push(self, value): # O(1)
        self.elements.append(value)
        self.size += 1

    def pop(self): # O(1)
        if not self.size:
            return "Stack is empty"
        self.elements.pop()
        self.size -= 1

    def getSize(self): # O(1)
        return self.size

    def isEmpty(self): # O(1)
        return not self.size

    def getTop(self): # O(1)
        if not self.size:
            return "Stack is empty"
        return self.elements[-1]

    def printStack(self): # O(n)
        if not self.size:
            return "Stack is empty"
        for i in range(self.size-1, -1, -1): # O(n)
            print(self.elements[i], end=" ")
