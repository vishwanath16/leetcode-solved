# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

def lengthOfLongestSubstring(s):
    charSet = set()
    res = 0
    l = 0
    
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        
        charSet.add(s[r])
        res =  max(res, len(charSet))

    return res



print(lengthOfLongestSubstring("pwwkew"))