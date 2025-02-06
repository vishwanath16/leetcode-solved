# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        twoSum = numbers[l] + numbers[r]
            
        if (twoSum < target):
            l += 1
        elif (twoSum > target):
            r -= 1
        else:
            return [l+1, r+1]


print(twoSum([2, 7, 11, 15], 9))
