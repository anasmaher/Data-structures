class node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None


def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def post(root):
    if root!=None:
        post(root.left)
        post(root.right)
        print(root.data)

def pre(root):
    if root!=None:
        print(root.data)
        pre(root.left)
        pre(root.right)