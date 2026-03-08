# Link: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

def checkOnesSegment(s):
    return "01" not in s

print(checkOnesSegment("11000"))