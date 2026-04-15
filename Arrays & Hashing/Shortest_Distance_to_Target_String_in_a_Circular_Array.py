# Link: https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

def closestTarget(words, target, startIndex):
    n = len(words)
    distances = []
    for i, w in enumerate(words):
        if w == target:
            distances.append(min(abs(i - startIndex), n - abs(i - startIndex)))
    return min(distances) if distances else -1

print(closestTarget(["a","b","leetcode", "leetcode", "easy"], "easy", 1))