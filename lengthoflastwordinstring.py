def lengthlast():

 s=" "
 c=0
 for i in range(len(s)-1,0,-1):
    if s[i]==' ':
        break
    else:
        c=c+1
 return c        

if __name__=='__main__':
   print(lengthlast())
