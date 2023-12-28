from sys import maxsize

def createstack():
    stack=[]
    return stack
def isempty(stack):
    return len(stack)==0
    
def push(stack,item):
    stack.append(item)
    print("pushed is"+item)

def pop(stack):
    if (isempty(stack)):
        return str(-maxsize-1)
    return stack.pop()
def peek(stack):
    if isempty(stack):
        return str(-maxsize-1)
    return stack[len(stack)-1]

if __name__=='__main__':
    stack=createstack()
    push(stack,str(10))
    push(stack,str(11))
    push(stack,str(15))
    push(stack,str(16))
    print(pop(stack))
    print(peek(stack))