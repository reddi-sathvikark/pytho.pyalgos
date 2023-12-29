def balanced(exp):
    stack=[]
    for i in range(len(exp)):
        if isopen(exp[i]):
            stack.append(exp[i])
        else:
             if stack and ((stack[-1] == '(' and exp[i] == ')') or
                          (stack[-1] == '{' and exp[i] == '}') or
                          (stack[-1] == '[' and exp[i] == ']')):
                   stack.pop()
             else:
                  return False 
             
                
    return not stack               
def isopen(ch):
     if ch=='[' or ch=='(' or ch=='{':
          return True
     else:
          return False
exp='({[]})'     
if balanced(exp):
     print("balanced")
else:
     print("not balanced")     
                       


