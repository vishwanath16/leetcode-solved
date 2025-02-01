# Link: https://leetcode.com/problems/binary-search/description/

def search(nums, target):
    l = 0
    r = len(nums) - 1

    for i in range(len(nums)):
        m = (l + r) // 2
        if(nums[m] == target):
            return m
        elif(nums[m] < target):
            l = m + 1
        elif(nums[m] > target):
            r = m - 1
            
    return -1

print(search([-1,0,3,5,9,12], 13))