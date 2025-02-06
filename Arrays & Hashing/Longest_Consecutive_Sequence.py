# Link: https://leetcode.com/problems/longest-consecutive-sequence/description/

def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0

    for i in nums:
        if (i-1) not in numSet:
            length = 0
            while (i + length) in numSet:
                length += 1

            longest = max(longest, length)
    
    return longest


print(longestConsecutive([100, 4, 200, 201, 202, 199, 198, 1, 3, 2]))