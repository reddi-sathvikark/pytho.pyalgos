def distinct(arr,n):
    j=0
    while j<=n:
        for i in range(j+1,n):
            if arr[i]!=arr[j]:
                print(arr[i])
                j=j+1

            
if __name__=='__main__':
    arr=[12,10,9,4,5,10,12,10,4,5]
    n=len(arr)
    distinct(arr,n)