class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linkedList(object):
    def __init__(self):
        self.root = None
        self.tail = None
        self.size = 0

    def addFront(self, data):
        newNode = Node(data)

        if not self.size:
            self.root = self.tail = newNode
            newNode.next = None
        else:
            newNode.next = self.root
            self.root = newNode
        self.size+=1

    def addLast(self, data):
        newNode = Node(data)

        if not self.size:
            self.root=self.tail=newNode
            newNode.next = None
        else:
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = None
        self.size+=1

    def insert(self, data, pos):
        if pos<=0 or pos>self.size+1:
            return print("Invalid position")

        newNode = Node(data)
        current = Node()

        if(pos==1):
            self.addFront(data)
        elif(pos==self.size+1):
            self.addLast(data)
        else:
            current = self.root
            for i in range(1,pos-1):
                current = current.next
            newNode.next = current.next
            current.next = newNode
        self.size+=1

    def printData(self):
        current = Node()
        current = self.root

        while current is not None:
            print(current.data)
            current = current.next

    def popFront(self):
        if not self.size:
            return
        elif self.size == 1:
            self.root=self.tail=None
            self.size-=1
        else:
            self.root = self.root.next
            self.size -=1

    def popLast(self):
        current = self.root.next
        prev = self.root
        if not self.size:
            return
        elif self.size==1:
            self.tail=self.root=None
            self.size-=1
        while current!=self.tail:
            prev = current
            current = current.next
        prev.next = None
        self.tail=prev
        self.size-=1

    def popByData(self, val):
        if not self.size:
            return
        elif self.root.data==val:
            self.root=self.root.next
            self.size-=1
            if not self.size:
                self.tail=None
        else:
            current = self.root.next
            prev = self.root
            while current!=None:
                if current.data==val:
                    prev.next=current.next
                    current.next=None
                    if self.tail==current:
                        self.tail=prev
                    self.size-=1
                    return
                else:
                    prev = current
                    current=current.next

    def popByPosition(self, pos):
        if pos<=0 or pos>self.size:
            return print("invalid position!")
        elif not self.size:
            return
        elif pos==1:
            self.root=self.root.next
            self.size-=1
            if not self.size:
                self.tail=None
        else:
            current = self.root.next
            prev = self.root
            for i in range(1, pos-1):
                prev = current
                current=current.next
            prev.next=current.next
            current.next=None
            if self.tail==current:
                self.tail=prev
            self.size-=1

# x = linkedList()
# x.addFront()
# x.addLast()
# x.insert()
# x.popFront()
# x.popLast()
# x.popByPosition()
# x.popByData()
# x.printData()
