# Link: https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/?envType=problem-list-v2&envId=pfdle0mr
# Solution Article: https://vishwanathts.hashnode.dev/solving-final-array-state-after-k-multiplication-operations-leetcode-solution

import heapq

def getFinalState(nums, k, multiplier):
    result = nums[::]

    min_heap = [(n, i) for i, n in enumerate(nums)]
    print(min_heap)
    heapq.heapify(min_heap)

    for _ in range(k):

        n, i = heapq.heappop(min_heap)
        result[i] *= multiplier
        heapq.heappush(min_heap, (result[i], i))

        

    return result

print(getFinalState([2,1,3,5,6], 5, 2))