# Link: https://leetcode.com/problems/length-of-last-word/description/
# Solution Article: https://vishwanathts.hashnode.dev/how-to-solve-add-binary-on-leetcode-a-step-by-step-guide

def lengthOfLastWord(s):
    return s.strip().split(" ")[-1]


print(lengthOfLastWord("   fly me   to   the moon  "))
