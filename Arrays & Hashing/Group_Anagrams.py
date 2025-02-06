# Link: https://leetcode.com/problems/group-anagrams/description/


#Method 1: Using Dictionary

def groupAnagrams(strs):
    result = {}

    for i in strs:
        key = ''.join(sorted(i))
        if key not in result:
            result[key] = []
        
        result[key].append(i)

    return list(result.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


#Method 2: Using DefaultDict

from collections import defaultdict

def groupAnagrams(strs):
    result = defaultdict(list)

    for i in strs:
        key = ''.join(sorted(i))
        result[key].append(i)

    return list(result.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))