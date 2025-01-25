# Link: https://leetcode.com/problems/sum-of-two-integers/description/

def getSum(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1  
    return a

print(getSum(2, 3))