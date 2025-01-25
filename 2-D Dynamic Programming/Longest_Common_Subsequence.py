# Link: https://leetcode.com/problems/longest-common-subsequence/description/

def longestCommonSubsequence(text1, text2):
    dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


text1 = "abcde"
text2 = "abce"
print(longestCommonSubsequence(text1, text2))
