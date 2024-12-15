# Link: https://leetcode.com/problems/climbing-stairs/description/
# Solution Article: https://vishwanathts.hashnode.dev/efficient-iterative-solution-for-climbing-stairs-problem-in-python

def climbStairs(n):

    x, y = 1, 1

    for i in range(n - 1):
        x, y = x + y, x
    
    return x

print(climbStairs(5))