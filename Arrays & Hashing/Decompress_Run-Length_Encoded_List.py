# Link: https://leetcode.com/problems/decompress-run-length-encoded-list/

def decompressRLElist(nums):
    result = []
    for i in range(0, len(nums), 2):
        result.extend(nums[i] * [nums[i+1]])

    return result


print(decompressRLElist([1,2,3,4]))