class node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None


#Check if balanced binary tree
def depth(root):
    if root == None:
        return 0
    return max(depth(root.left), depth(root.right)) + 1

def ch(root):
    if root == None:
        return True
    return ch(root.left) and ch(root.right) and abs(depth(root.left)-depth(root.right)) <= 1