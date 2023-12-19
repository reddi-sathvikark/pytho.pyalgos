def rearrange(arr,n):
    
    for i in range(n):
      if (i%2==0):
        if(arr[i]<arr[i-1]):
           arr[i-1],arr[i]=arr[i],arr[i-1]
      else:
         if(arr[i]>arr[i-1]):
            arr[i-1],arr[i]=arr[i],arr[i-1]
if __name__=='__main__':
   arr=[1,2,2,1]
   n=len(arr)
   rearrange(arr,n)
   for i in range(n):
      print(arr[i])              