# Link: https://leetcode.com/problems/number-of-1-bits/description/
# Solution Article: https://vishwanathts.hashnode.dev/why-pythons-built-in-functions-outperform-manual-optimization

# Method 1:

def hammingWeight(n):
    return list(bin(n)[2:]).count("1")

print(hammingWeight(5))


# Method 2 (BitWise):

def hammingWeight(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

print(hammingWeight(5))



