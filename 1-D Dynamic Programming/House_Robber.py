# Link: https://leetcode.com/problems/house-robber/description/

def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev_max, current_max = 0, nums[0]
    
    for i in range(1, len(nums)):
        new_max = max(current_max, nums[i] + prev_max)
        prev_max = current_max
        current_max = new_max
    
    return current_max


print(rob([1,2,3]))