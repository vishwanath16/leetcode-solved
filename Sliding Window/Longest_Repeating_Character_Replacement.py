# Link: https://leetcode.com/problems/longest-repeating-character-replacement/description/

# Method 1

def characterReplacement(s, k):
    res = 0
    count = {}
    l = 0
    maxf = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])
        while((r - l) + 1 - maxf > k):
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)

    return res
            
            
print(characterReplacement('ABABB', 1))


# Method 2

def characterReplacement(s, k):
    res = 0
    count = {}
    l = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        while((r - l) + 1 - max(count.values()) > k):
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)

    return res
            
            
print(characterReplacement('ABABB', 1))