def element():
    nums=[1,3,5,6]
    target=2
    for i in range(len(nums)-1):
        if nums[i]==target:
           print(i)
        else:
            if nums[i]<target<nums[i+1]:
                print("at index",i+1)
element()