def reverse(arr,start,end):
    while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start=start+1
            end=end-1

if __name__=='__main__':
      arr=[1,2,3,4,5,6]
      print(arr)
      reverse(arr,0,len(arr)-1)
      print(arr)



    