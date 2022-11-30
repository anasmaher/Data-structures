class node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None


# Check if prefect binary tree
def depth(node):
    d = 0
    while node!=None:
        d+=1
        node = node.left
    return d

def ch(root, d, l=0):
    if root==None:
        return True
    if root.left==None and  root.right==None:
        if d==l+1:
            return True
        else:
            return False
    if (root.left==None and root.right!=None) or (root.left!=None and root.right==None):
        return False

    return ch(root.left, d, l+1) and ch(root.right, d, l+1)