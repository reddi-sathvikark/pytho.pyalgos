class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def height(root):
    if root is None:
        return 0
    return max(height(root.left),height(root.right))+1
def isbalanced(root):
    if root is None:
        return True
    lh=height(root.left)
    rh=height(root.right)
    if(abs(lh-rh<=1))and isbalanced(root.left) is True and isbalanced(root.right) is True:
        return True
    return False
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.left.left.left=node(8)
if isbalanced(root):
    print("balanced tree")
else:
    print("not balanced")    

    
            