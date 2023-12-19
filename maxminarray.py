class pair:
    def __init__(self):
        self.min=0
        self.max=0

def getminmax(arr,n):
    minmax=pair()        
    if n==1:
        minmax.min=arr[0]
        minmax.max=arr[0]
    if arr[0]>arr[1]:
        minmax.min=arr[1]
        minmax.max=arr[0]
    else:
        minmax.min=arr[0]
        minmax.max=arr[1]
    for i in range(2,n-1):
        if arr[i]>minmax.max:
            minmax.max=arr[i] 
        elif arr[i]<minmax.min:
            minmax.min=arr[i]
    return minmax

if __name__=='__main__':
    arr=[1,2,4,3,6,7]
    n=len(arr)
    minmax=getminmax(arr,n+1)
    print("minimum is",minmax.min)
    print("maximum is",minmax.max)        
