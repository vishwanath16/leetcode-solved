# Link: https://leetcode.com/problems/contains-duplicate/description/

def containsDuplicate(nums):
    return len(nums) != len(set(nums))

print(containsDuplicate([1,2,3,1]))