# Link: https://leetcode.com/problems/counting-bits/description/

# Method 1:

def countBits(n):
    lis = []
    
    for i in range(n+1):
        lis.append(list(bin(i)[2:]).count("1"))

    return lis

print(countBits(5))


# Method 2 (BitWise):

def countBits(n):
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        num = i
        while num != 0:
            res[i] += 1
            num &= (num - 1)
    return res

print(countBits(5))


