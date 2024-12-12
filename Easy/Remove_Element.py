# Link: https://leetcode.com/problems/remove-element/description/

def removeElement(nums, val):
    i = 0

    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]

            i = i + 1

    return i


print(removeElement([3, 2, 2, 3], 3))
