def majority(arr,n):
    maxcount=0
    index=-1
    for i in range(n):
     count=1
     for j in range(i+1,n):
        if arr[i]==arr[j]:
           count=count+1

     if (count>maxcount):
        maxcount=count
        index=i
    if (maxcount>n//2):
        print(arr[index])
    else:
        print("no majority")
if __name__=='__main__':
     arr=[2,2,3,3,4,4,5,4,4,4,4]      
     n=len(arr)
     majority(arr,n)  
              
