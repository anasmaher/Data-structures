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

# Undo Redo using stack

def ur():
    undo = Stack()
    redo = Stack()

    print("Enter words or 'u' to undo, 'r' to redo, 'p' to print text, 'e' to exit: ", end="")
    while True:
        val = input()
        if val == "u":
            if undo.getSize()==0:
                continue
            else:
                redo.push(undo.pop())
        elif val == "r":
            if redo.getSize()==0:
                continue
            else:
                undo.push(redo.pop())
        elif val == "p":
            undo.printStack()
        elif val == "e":
            break
        else:
            undo.push(val)

ur()