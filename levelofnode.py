class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def getleveluntil(node,data,level):
        if node==None:
             return 0
        if node.data==data:
            return level
        downlevel=getleveluntil(node.left,data,level+1)
        if downlevel!=0:
            return downlevel
        downlevel=getleveluntil(node.right,data,level+1)
        
        return downlevel
               
        
def getLevel(node, data):
 
      return getleveluntil(node, data, 1)
 
 
# Driver Code
if __name__ == '__main__':
 
    # Let us construct the Tree shown
    # in the above figure
    root = Node(3)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(4)
    for x in range(1, 6):
        level = getLevel(root, x)
        if (level):
            print("Level of", x,
                  "is", getLevel(root, x))
        else:
            print(x, "is not present in tree")