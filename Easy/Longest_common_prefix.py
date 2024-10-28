# Link: https://leetcode.com/problems/longest-common-prefix/description/

def longestCommonPrefix(strs):
    common = ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return common
            
        common += strs[0][i]
        
    return common

print(longestCommonPrefix(["flower","flow","flight"]))