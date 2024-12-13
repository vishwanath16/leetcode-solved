# Link: https://leetcode.com/problems/add-binary/description/
# Solution: https://leetcode.com/problems/add-binary/solutions/6144247/python-one-liner-solution-add-binary-pro-tp54

def addBinary(a, b):

    return format(int(a, 2) + int(b, 2), 'b')

print(addBinary("1010", "1011"))
