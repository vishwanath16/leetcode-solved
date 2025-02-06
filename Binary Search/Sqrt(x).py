# Link: https://leetcode.com/problems/sqrtx/description/
# Solution Article: https://vishwanathts.hashnode.dev/how-to-solve-the-square-root-of-x-using-pythons-binary-search

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

