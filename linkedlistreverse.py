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
    def reverse(self):
        prev=None
        current=self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev 

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

if __name__=='__main__':
    llist=linkedlist()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    print ("Given linked list")
    llist.printList()
    llist.reverse()
    print ("\nReversed linked list")
    llist.printList()

