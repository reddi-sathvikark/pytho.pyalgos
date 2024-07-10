class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class solution:
    def isbalanced(self,root):
        return (self.height(root)>=0)        
    def height(self,root):
        if root is None:
            return 0
        leftheight=self.height(root.left)
        rightheight=self.height(root.right)
        if leftheight<0 or rightheight<0 or abs(leftheight-rightheight)>1:
            return -1
        else:
           return max(leftheight,rightheight)+1

root=node(1)
root.left=node(2)
root.right=node(6)
root.left.left=node(4)   
root.left.left.left=node(9)
root.left.left.left.left=node(10)
obj=solution()
ans=obj.isbalanced(root)
print(ans)