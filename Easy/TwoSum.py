def twoSum(nums, target):
    hash = {}
    for i, n in enumerate(nums):
        diff = target - n
        print("hash: ", hash)
        print("diff: ", diff)
        if diff in hash:
            return [hash[diff], i]
        else:
            hash[n] = i



print(twoSum([2,1,5,3], 4))

