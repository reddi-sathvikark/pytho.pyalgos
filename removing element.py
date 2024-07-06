def remove(nums):
    k=3
    c=0
    for i in range(0,len(nums)-1):
        if nums[i]==k:
            nums.pop(i)
            c=c+1  
    return c
    
if __name__=='__main__':
    nums=[3,2,2,3]
    print(remove(nums))
    print(nums)            
