# Link: https://leetcode.com/problems/isomorphic-strings/

def isIsomorphic(s, t):
    dict1 = dict()
    dict2 = dict()

    for i in range(len(s)):
        if (s[i] in dict1 and dict1[s[i]] != t[i]) or (t[i] in dict2 and dict2[t[i]] != s[i]):
            return False
        dict1[s[i]] = t[i]
        dict2[t[i]] = s[i]


    return True

print(isIsomorphic("badc", "baba"))

        