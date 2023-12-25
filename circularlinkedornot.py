class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
def circular(head):
    if head==None:
        return True
    Node=head.next
    i=0
    while((Node is not  None)and Node is not head):
        i=i+1
        Node=Node.next
    return(Node==head)
if __name__=='__main__':
    llist=linkedlist()
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)
    fourth=Node(4)

    llist.head.next=second
    second.next=third
    third.next=fourth

    if(circular(llist.head)):
        print("yes")
    else:
        print("no")
    fourth.next=llist.head 
    if(circular(llist.head)):
        print("yes" )
    else:
        print("no")           


