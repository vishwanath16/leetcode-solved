# Link: https://leetcode.com/problems/decode-ways/description/

def numDecodings(s):
    if not s or s[0] == '0':
        return 0

    prev2, prev1 = 1, 1  # dp[i-2] and dp[i-1]

    for i in range(1, len(s)):
        curr = 0
        if s[i] != '0':
            curr += prev1  # Single character decoding
        if 10 <= int(s[i - 1:i + 1]) <= 26:
            curr += prev2  # Two-character decoding
        prev2, prev1 = prev1, curr  # Update for next iteration

    return prev1



print(numDecodings("1220"))