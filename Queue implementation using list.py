class queue():
    def __init__(self):
        self.size = 0
        self.queue = []

    def enq(self, val):
        self.queue.append(val)
        self.size+=1

    def deq(self):
        if not self.size:
            return print("queue is empty")
        self.queue.pop(0)
        self.size-=1

    def getFront(self):
        if not self.size:
            return print("queue is empty")
        return self.queue[0]

    def getBack(self):
        if not self.size:
            return print("queue is empty")
        return self.queue[-1]

    def getSize(self):
        return self.size

    def print(self):
        for i in self.queue:
            print(i, end=" ")
        print()

# q = queue()
# q.enq()
# q.deq()
# q.getBack()
# q.getFront()
# q.getSize()
# q.print()