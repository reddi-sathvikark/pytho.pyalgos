class stacknode:
    def __init__(self,data):
        self.data=data
        self.next=next

class stack:
    def __init__(self):
        self.root=None
    def isempty(self):
        return True if self.root is None else False
    def push(self,data):
        newnode=stacknode(data)
        newnode.next=self.root
        self.root=newnode
        print("push is",data)
    def pop(self):
        if stack.isempty():
            return float("-inf")
        temp=self.root
        self.root=self.root.next
        popped= temp.data
        return popped
    def peek(self):
        if stack.isempty():
            return float("-inf")
        return self.root.data
if __name__=='__main__':
    stack=stack()
    stack.push(10)
    stack.push(20)
    stack.push(50)
    stack.push(30) 
    print(stack.pop())
    print(stack.peek())
    