class Node:
 def __init__(self,key):
    self.key= key
    self.child=[]
def new_node(key):
    temp=  Node(key)   
    return temp
def depth_of_tree(ptr):
    if ptr is None:
        return 0 
    else:
        maxdepth=0
        for child in ptr.child:
            maxdepth=max(maxdepth,depth_of_tree(child))
        return maxdepth+1
if __name__=='__main__':
    root=new_node('A')
    root.child.extend([new_node('B'),new_node('C'),new_node('D'),new_node('E')])
    root.child[0].child.extend([new_node('K'), new_node('J')]) 
    root.child[2].child.append(new_node('G')) 
    root.child[3].child.extend([new_node('C'), new_node('H'), new_node('I')]) 
    root.child[0].child[0].child.extend([new_node('N'), new_node('M')]) 
    root.child[3].child[2].child.append(new_node('L')) 
  
    print(depth_of_tree(root)) 



            
