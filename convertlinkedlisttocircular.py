class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def push(head,data):
    if not head:
        return node(data)
    
    newnode=node(data)
    newnode.next=head
    head=newnode
    return head
def circular(head):
    start=head
    while(head.next!=None):
        head=head.next

    head.next=start
    return start
def displaylist(node):
    start=node
    while(node.next is not start):
        print(node.data)
        node=node.next
    print(node.data)


if __name__=='__main__':
    head=None
    head=push(head,15)
    head=push(head,21)
    head=push(head,16)
    head=push(head,27)
    head=push(head,18)

    circular(head)
    print("displaylist")
    displaylist(head)            
