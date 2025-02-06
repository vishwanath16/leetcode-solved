# https://leetcode.com/problems/ransom-note/description/

from collections import Counter

def canConstruct(ransomNote, magazine):
    return not (Counter(ransomNote) - Counter(magazine))


print(canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj")) 