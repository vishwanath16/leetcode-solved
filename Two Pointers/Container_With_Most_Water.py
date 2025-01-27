# Link: https://leetcode.com/problems/container-with-most-water/description/

# Brute Force Solution

def maxArea(height):
    l = 0
    r = l + 1
    res = 0

    for l in range(len(height)):
        for r in range(l + 1, len(height)):
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

    return res

print(maxArea([1,8,6,2,5,4,8,3,7]))



# Linear Time Solution

def maxArea(height):
    l = 0
    r  =len(height) - 1
    res = 0
    
    while l < r:
        area = (r - l)  * min(height[r], height[l])
        res = max(res, area)

        if(height[l] < height[r]):
            l += 1
        else: 
            r -= 1
    
    return res

print(maxArea([8,7,2,1]))