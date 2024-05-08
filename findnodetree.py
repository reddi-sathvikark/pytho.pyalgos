class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def findnode(root,x):
    if root==None:
        return False
    if root.data==x:
        return True
    ans1=findnode(root.left,x)
    if ans1:
        return True
    ans2=findnode(root.right,x)
    
    return ans2
if __name__=='__main__':
    root=Node(0)
    root.left = Node(1) 
    root.left.left = Node(3) 
    root.left.left.left = Node(7) 
    root.left.right = Node(4) 
    root.left.right.left = Node(8) 
    root.left.right.right = Node(9) 
    root.right = Node(2) 
    root.right.left = Node(5) 
    root.right.right = Node(6) 
    x=4
    if (findnode(root,x)):
        print("yes")
    else:
        print("no")    
