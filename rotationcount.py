def rotationcount(arr,n):
    min=arr[0]
    mim_indx=0
    for i in range(0,n):
        if min>arr[i]:
            min=arr[i]
            min_indx=i

    return min_indx
if __name__=='__main__':
    arr=[15,18,2,3,4,5,6]
    n=len(arr)
    print(rotationcount(arr,n))