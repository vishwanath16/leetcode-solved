# Link: https://leetcode.com/problems/reorganize-string/description/

import heapq
from collections import Counter

def reorganizeString(s):
    count = Counter(s)
    maxHeap = [[-cnt, char] for char, cnt in count.items()]
    heapq.heapify(maxHeap)
    
    prev = None
    res = ''

    while maxHeap or prev:
        if prev and not maxHeap:
            return ''

        cnt, char = heapq.heappop(maxHeap)
        res += char
        cnt += 1

        if prev:
            heapq.heappush(maxHeap, prev)
            prev = None

        if cnt != 0:
            prev = [cnt, char]

    return res

print(reorganizeString('aabklllsssdthrw'))