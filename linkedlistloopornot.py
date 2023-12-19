class node:
    def __init__(self,data):
        self.data=data
        self.next=next
class linkedlist:
    def __init__(self):
        self.head=None
    def push(self,newdata):
        newnode=node(newdata)
        newnode.next=self.head
        self.head=newnode

    def detectloop(self):
        temp=self.head
        s=set()
        while(temp):
            if (temp in s):
                return True
            s.add(temp)
            temp=temp.next

        return False
if __name__=='__main__':
    llist=linkedlist()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(10)
    llist.head.next.next.next.next=llist.head
    print(llist.detectloop())      