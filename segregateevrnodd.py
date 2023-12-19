def evenodd(arr):
    even=[x for x in arr %2==0]
    odd=[x for x in arr%2!=0]
    arr=even+odd
if __name__=='__main__':
    arr=[2,4,6,7,8,9,1,3,5]
    n=len(arr)  
    evenodd(arr) 
    for i in range(n):
        print(arr[i]) 