class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class nodeoperation:
    def pushnode(self,headref,data_val):
        newnode=node(data=data_val)
        newnode.next=headref[0]
        headref[0]=newnode
if __name__=='__main__':
   head=[None]
   temp=nodeoperation()
   for i in range(5,0,-1):
       temp.pushnode(head,i)
   v=[]
   while head[0]:
       v.append(head[0].data)
       head[0]=head[0].next
   print(v[len(v)//2])        
