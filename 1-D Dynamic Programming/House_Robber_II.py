# Link: https://leetcode.com/problems/house-robber-ii/description/

def rob(nums):
    if len(nums) <= 3:
        return max(nums)

    return max(helper(nums[1:]), helper(nums[:-1]))

def helper(nums):
    prev_max, current_max = 0, nums[0]

    for i in range(1, len(nums)):
        new_max = max(current_max, nums[i] + prev_max)
        prev_max = current_max
        current_max = new_max

    return current_max 
        

print(rob([2,3,2]))