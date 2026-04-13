# Link: https://leetcode.com/problems/fibonacci-number/

def fib(n):
    if n == 0:
        return 0

    lis = [0, 1]

    for i in range(1, n-1):
        lis.append(lis[-1] + lis[-2])

    return sum(lis[-2:])

print(fib(4))