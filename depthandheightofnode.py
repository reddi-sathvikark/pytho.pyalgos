class Node:
    def __init__(self,k):
        self.data=k
        self.left=None
        self.right=None
def finddepth(root,k):
    if root==None:
        return -1
    dist=-1
    if root.data==k:
        return dist+1
    dist=finddepth(root.left,k)
    if dist>=0:
        return dist+1
    dist=finddepth(root.right,k)
    if dist>=0:
        return dist+1
    return dist+1
def heightuntil(root,k):
    global height
    if (root==None):
      return -1
    leftheight=heightuntil(root.left,k)
    rightheight=heightuntil(root.right,k)
    ans=max(leftheight,rightheight)+1
    if root.data==k:
        height=ans
    return ans
def findheight(root,k):
    global height
    maxheight=heightuntil(root,k)
    return height    
if __name__=='__main__':
    height=-1
    root=Node(5)
    root.left=Node(10)
    root.right=Node(15)
    root.left.left=Node(20)
    root.left.right=Node(25)
    root.left.right.right=Node(45)
    root.right.left=Node(30)
    root.right.right=Node(35)
    k=25
    print("depthof treenode is",finddepth(root,k))
    print("height of node is",findheight(root,k))

