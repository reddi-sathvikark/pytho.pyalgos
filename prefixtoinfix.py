def prefixtoinfix(exp):
    stack=[]
    i=len(exp)-1
    while(i>=0):
        if not isoperator(exp[i]):
            stack.append(exp[i])
            i=i-1

        else:
            str="(" + stack.pop() +exp[i] + stack.pop() + ")"
            stack.append(str)
            i=i-1
    return stack.pop()    
def isoperator(c):
    if c=='+'or c=='-'or c=='*' or c=='/' or c=='^' or c=='('or c==')' :
        return True
    else:
        return False
if __name__=='__main__':

  str="*-A/BC-/AKL"
  print(prefixtoinfix(str))
                          