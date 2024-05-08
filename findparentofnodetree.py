class Node:
   
    def __init__(self, data):
       
        self.data = data
        self.left = None
        self.right = None
def findparent(node:Node,
               val: int,
               parent: int)->None:
    if node==None:
        return 
    if node.data==val:
        print(parent)
    else:
        findparent(node.left,val,node.data)
        findparent(node.right,val,node.data)
if __name__=='__main__':
    root=Node(1)   
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    node = 3
    findparent(root,node,-1)
    
