# Link: https://leetcode.com/problems/maximum-product-subarray/description/

def maxProduct(nums):
    res = max(nums)
    curMax, curMin = 1, 1

    for n in nums:
        if n == 0:
            curMin, curMax = 1, 1
            continue

        temp = n * curMax
        curMax = max(n, n * curMax, n * curMin)
        curMin = min(n, n * curMin, temp)
        res = max(res, curMax)

    return max(res, curMax)


print(maxProduct([2,3,-2,4,-8,-2]))