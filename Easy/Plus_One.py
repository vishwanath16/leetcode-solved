#Link: https://leetcode.com/problems/plus-one/description/

def plusOne(digits):
    increment = int(''.join(map(str, digits))) + 1
    return list(map(int, str(increment)))

print(plusOne([1, 2, 9]))