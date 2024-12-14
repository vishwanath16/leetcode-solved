# Link: https://leetcode.com/problems/sqrtx/description/
#Solution: https://leetcode.com/problems/sqrtx/solutions/6145109/efficient-binary-search-solution-find-sq-irhk

def mySqrt(x):
    left, right = 0, x
    result = 0
    while left <= right:
        mid = (left + right) // 2

        if mid**2 > x:  
            right = mid - 1
        
        elif mid**2 < x:         
            left = mid + 1
            result = mid
        else:
            return mid
        
    return result



print(mySqrt(10))

