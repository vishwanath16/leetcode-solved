# Link: https://leetcode.com/problems/majority-element/

def majorityElement(nums):
    res, count = 0, 0

    for num in nums:
        if count == 0:
            res = num
            count = 1
        elif num == res:
            count += 1
        else:
            count -= 1
    
    return res

print(majorityElement([2,2,1,1,1,2,2,1]))