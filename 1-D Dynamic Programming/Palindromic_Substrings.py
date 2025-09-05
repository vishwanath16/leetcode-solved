# Link: https://leetcode.com/problems/palindromic-substrings/description/

def countSubstrings(s):
    def countPali(s, l, r):
        res = 0
        while l >=0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

    res = 0
    for i in range(len(s)):
        # to count odd number of palindromes
        res += countPali(s, i, i)
        # to count even number of palindromes
        res += countPali(s, i, i + 1)

    return res

# Test
s = "abb"
print(countSubstrings(s))  