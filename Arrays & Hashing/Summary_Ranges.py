# Link: https://leetcode.com/problems/summary-ranges/

def summaryRanges(nums):
    res = []
    start = 0
    for i in range(len(nums)):
        if(i == len(nums) - 1 or nums[i+1] != 1 + nums[i]):
            if start == i:
                res.append(f'{nums[i]}')
            else:
                res.append(f'{nums[start]}->{nums[i]}')

            start = i+1

    return res

print(summaryRanges([0,2,3,4,6,8,9,11]))
