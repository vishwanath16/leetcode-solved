# Link: https://leetcode.com/problems/plus-one/description/
# Solution Article: https://vishwanathts.hashnode.dev/step-by-step-guide-to-solve-leetcodes-plus-one-problem-using-pythons-map-function

def plusOne(digits):
    increment = int(''.join(map(str, digits))) + 1
    return list(map(int, str(increment)))

print(plusOne([1, 2, 9]))