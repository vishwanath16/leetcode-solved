# Link: https://leetcode.com/problems/add-binary/description/
# Solution Article: https://vishwanathts.hashnode.dev/how-to-solve-add-binary-on-leetcode-a-step-by-step-guide

def addBinary(a, b):

    return format(int(a, 2) + int(b, 2), 'b')

print(addBinary("1010", "1011"))
