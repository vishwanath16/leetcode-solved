# Link: https://leetcode.com/problems/climbing-stairs/description/
# Solution Article: 

from itertools import product

def climbStairs(n):

    perms = product(range(1, n + 1), repeat=2)
    return len(list(perms))


print(climbStairs(4))