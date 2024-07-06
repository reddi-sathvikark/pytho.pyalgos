class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class linkedlist:
    def __init__(self):
        self.head=None
    def push(self,newdata):
        new_node=node(newdata)
        new_node.next=self.head
        self.head=new_node


    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next
        
    def removeduplicates(self):
        temp=self.head
        if temp is None:
            return
        while temp.next is not None:
          if temp.data==temp.next.data:
            new=temp.next
            new.next=None
            temp.next=temp.next.next
            
          else:
            temp=temp.next 
        return self.head                 
llist=linkedlist()
llist.push(1)
llist.push(1)
llist.push(2)
llist.push(3)    
llist.removeduplicates()
llist.printList()        



                   