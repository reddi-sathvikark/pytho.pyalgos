def reverse(arr,start,end):
    while(start<end):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start=start+1
        end=end-1
def leftrotate(arr,d,n):
    if d==0:
        return
    d=d%n
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)

if __name__=='__main__':
    arr=[1,2,3,4,5,6,7]
    n=len(arr)
    d=2
    leftrotate(arr,d,n)

    print(arr)    