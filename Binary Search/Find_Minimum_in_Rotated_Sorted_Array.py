# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if(nums[mid] > nums[right]):
            left = mid + 1
        else:
            right = mid

    return nums[left]


print(findMin([3,4,5,1,2])) #Rotated 3 times
