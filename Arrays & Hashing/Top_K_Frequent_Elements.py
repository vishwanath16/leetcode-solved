# Link: https://leetcode.com/problems/top-k-frequent-elements/description/

from collections import Counter

def topKFrequent(nums, k):
    counts = Counter(nums)
    
    # Sort keys by frequency (counts) in descending order
    sorted_keys = sorted(counts.keys(), key= lambda x : counts[x], reverse=True)
    
    print(sorted_keys)

    # Return the top k keys
    return sorted_keys[:k]


print(topKFrequent([4,1,-1,2,-1,2,3], 2))

