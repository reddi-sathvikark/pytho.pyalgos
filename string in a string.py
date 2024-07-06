def printindex(s,sub):
    flag=False
    for i in range(len((s))):
      if s[i:i+len(sub)]==sub:
         print(i)
         flag=True
         break
    if flag==False:
       print(None)
if __name__=='__main__':
   haystack="sadbutsad"
   needle="sad"
   printindex(haystack,needle)          