class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def pushnode(head_ref,data):
    temp=head_ref
    ptr1=node(0)
    ptr1.data=data
    ptr1.next=head_ref

    if(head_ref!=None):
        while(temp.next!=head_ref):
            temp=temp.next
        temp.next=ptr1
    else:
        ptr1.next=ptr1

    head_ref=ptr1
    return head_ref

def count(head):
    temp=head
    result=0
    if(head!=None):
        while True:
            temp=temp.next
            result=result+1
            if(temp==head):
                break
    return result

if __name__=='__main__':

    head=None
    head=pushnode(head,10)
    head=pushnode(head,12)
    head=pushnode(head,14)
    head=pushnode(head,19)

    print(count(head))
        


