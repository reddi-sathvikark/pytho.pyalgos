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
    def getcount(self):
        count=0
        temp=self.head 
        while(temp):
            count=count+1
            temp=temp.next
        return count
if __name__=='__main__':
    llist=linkedlist()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    print(llist.getcount())                   