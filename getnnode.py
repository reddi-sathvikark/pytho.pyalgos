class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
    def push(self,newdata):
        newnode=node(newdata)
        newnode.next=self.head
        self.head=newnode
    def getnnode(self,index):
     current=self.head
     count=0  
     while(current):
        if count==index:
            return current.data
        count=count+1
        current=current.next
if __name__=='__main__':
    llist=linkedlist()
    llist.push(1)
    llist.push(3)
    llist.push(4)
    llist.push(6)
    llist.push(7)
    n=2
    print(llist.getnnode(n))             