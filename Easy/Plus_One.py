#Link: https://leetcode.com/problems/plus-one/description/
#Solution: https://leetcode.com/problems/plus-one/solutions/6144229/fastest-python-one-liner-plus-one-proble-qo8f

def plusOne(digits):
    increment = int(''.join(map(str, digits))) + 1
    return list(map(int, str(increment)))

print(plusOne([1, 2, 9]))