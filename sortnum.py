def sortnum(arr,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]


if __name__=='__main__':
    arr=[0,1,2,0,1,2]
    n=len(arr)
    sortnum(arr,n)
    print(arr)