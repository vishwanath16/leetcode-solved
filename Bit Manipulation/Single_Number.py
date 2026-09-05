# Link: https://leetcode.com/problems/single-number/

def singleNumber(nums) -> int:
    res = 0
    for n in nums:
        res = n ^ res
    
    return res


print(singleNumber([1,2,1,2,4]))