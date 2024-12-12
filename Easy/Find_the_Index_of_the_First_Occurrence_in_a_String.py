# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

def strStr(haystack, needle):

    for i in range(len(haystack) + 1 - len(needle)):
        for j in range(len(needle)):
            if(haystack[i + j] != needle[j]):
                break

            if j == len(needle) - 1:
                return i


print(strStr('chooleetcode', 'leet'))








