# Link: https://leetcode.com/problems/length-of-last-word/description/

def lengthOfLastWord(s):
    return s.strip().split(" ")[-1]


print(lengthOfLastWord("   fly me   to   the moon  "))
