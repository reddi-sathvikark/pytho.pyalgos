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
    def search(self):
        x=14
        temp=self.head
        while(temp):
            if (temp.data==x):
                return True
            temp=temp.next
        return False
if __name__=='__main__':
    lists=linkedlist()
    lists.push(1)
    lists.push(14)        
    lists.push(3)
    lists.push(5)
    lists.push(10)
    print(lists.search())