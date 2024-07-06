open_list=['[','{','('] 
close_list=[']','}',')']


def balance(str):
  stk=[]
  for i in str:
    if i in open_list:
      stk.append(i)
    elif i in close_list:
      pos=close_list.index(i)  
      if open_list[pos]==stk[len(stk)-1]:
        stk.pop()
      else:
        return "unbalanced"
  if len(stk)==0:
    return "balanced"
  else:
    return "unbalanced"

str='()'
print(balance(str))      