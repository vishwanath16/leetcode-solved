# Link: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

def minOperations(s):
    count = 0

    for i in range(len(s)):
        if i % 2:
            count += 1 if(s[i] == '0') else 0
        else:
            count += 1 if(s[i] == '1') else 0

    return min(count, len(s) - count)


print(minOperations("10"))