# Link: https://leetcode.com/problems/length-of-last-word/description/
# Solution: https://leetcode.com/problems/length-of-last-word/solutions/6144204/python-one-liner-solution-beats-100-runt-3adn

def lengthOfLastWord(s):
    return s.strip().split(" ")[-1]


print(lengthOfLastWord("   fly me   to   the moon  "))
