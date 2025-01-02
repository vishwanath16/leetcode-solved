# Link: https://leetcode.com/problems/missing-number/description/

def missingNumber(nums):
    nums = sorted(nums)
    for i in range(len(nums)):
        if nums[i] != i:
            return i
        
    return len(nums)


print(missingNumber([9,6,4,2,3,5,7,0,1,10]))