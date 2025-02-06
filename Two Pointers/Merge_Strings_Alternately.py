# Link: https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

def mergeAlternately(word1, word2):
    result = ''
    for i, j in zip(word1, word2):
        result += i + j

    result += word2[len(word1):]
    result += word1[len(word2):]

    return result


print(mergeAlternately("Hello", "World"))
