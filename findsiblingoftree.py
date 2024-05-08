from collections import deque
class Node:
    def __init__(self,key):
        self.key=key
        self.child=[]
def newnode(key):
    temp=Node(key)   
    return temp
def findsibling(root,value):
    flag=0
    if root==None:
        return
    
    q=deque()
    q.append(root)
    while(len(q)>0):
        temp=q.popleft()
        for i in range(len(temp.child)):
            if temp.child[i].key==value:
                flag=1
                for j in range(len(temp.child)):
                  if value!=temp.child[j].key :
                    print(temp.child[j].key)
                break
            q.append(temp.child[i])
    if flag==0:
        print("no siblings")


def constructTree():
    root = Node(10)
    root.child.append(Node(20))
    root.child.append(Node(30))
    root.child.append(Node(40))
    root.child[0].child.append(Node(50))
    root.child[0].child.append(Node(60))
    root.child[1].child.append(Node(70))
    root.child[1].child.append(Node(80))
    root.child[2].child.append(Node(90))
    root.child[2].child.append(Node(100))
    root.child[2].child.append(Node(110))
 
    return root
 
# Driver Code
if __name__ == '__main__':
   
    # Stores root of the
    # constructed tree
    root = constructTree()
 
    X = 30
     
    # Print siblings of Node X
    findsibling(root, X)