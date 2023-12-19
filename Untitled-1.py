def missing(arr,n):
    i=1
    while(i!=n+1):
     for item in arr:
        if i==item:
            i=i+1
        else:
            return i

if __name__=='__main__':
    arr=[1,2,3,5]
    n=len(arr)
    a=missing(arr,n)
    print(a)            