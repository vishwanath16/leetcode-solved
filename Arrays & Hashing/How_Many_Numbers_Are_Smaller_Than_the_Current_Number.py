# Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

def smallerNumbersThanCurrent(nums):
    res = {}
    result = []

    for i, n in enumerate(sorted(nums)):
        if n not in res:
            res[n] = i

    for i in nums:
        result.append(res[i])

    return result

print(smallerNumbersThanCurrent([8,1,2,2,3]))