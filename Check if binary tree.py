class node:
	 def __init__(self, data=None):
	 self.data = data
	 self.child = []

def isBinary(root):
	 if root==None:
		 return True

	 q = []
	 q.append(root)
	 while(len(q)):
		 n=len(q)
		 while(n):
			 p = q.pop(0)
			 if p.data==None:
				 if len(p.child) > 2:
				 	return False
			 i=0
			 while i<len(p.child):
			 	q.append(p.child[i])
			 	i+=1
			 n-=1
	 return True
