def sortstack(stack):
    tmpstack=createstack()
    while(isempty(stack)==False):
        tmp=top(stack)
        pop(stack)
        while(isempty(tmpstack)==False and int(top(tmpstack))<int(tmp)):
            push(stack,top(tmpstack))
            pop(tmpstack)
        push(tmpstack,tmp)
    return tmpstack
def createstack():
    stack = []
    return stack
def isempty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
def top(stack):
    p=len(stack)
    return stack[p-1]
def pop(stack):
    if (isempty(stack)):
        print("underflow")

    return stack.pop()
def prints(stack):
    for i in range(len(stack)-1,-1,-1) :
        print(stack[i])
    print()
stack = createstack()
push( stack, str(34) )
push( stack, str(3) )
push( stack, str(31) )
push( stack, str(98) )
push( stack, str(92) )
push( stack, str(23) )
 
print("Sorted numbers are: ")
sortedst = sortstack ( stack )
prints(sortedst)                       