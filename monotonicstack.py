def increasingstack(arr,n):
    stk=[]
    for i in range(n):
        while(len(stk)>0 and stk[len(stk)-1]>arr[i]):
            stk.pop()
        stk.append(arr[i])
    N2=len(stk)
    ans=[0]*N2
    j=N2-1
    while(len(stk)!=0):
        ans[j]=stk[len(stk)-1]
        stk.pop()
        j=j-1        
    for i in range(n):
        print(arr[i])
    for i in range(N2):
        print(ans[i])    

arr=[1,4,3,12,10]
n=len(arr)
increasingstack(arr,n)        