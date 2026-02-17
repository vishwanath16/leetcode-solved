# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

def search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (high + low) // 2
        if nums[mid] == target:
            return mid
        
        if nums[low] <= nums[mid]:
            if target > nums[mid] or target < nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if target > nums[mid] or target < nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

print(search([30,40,50,5,10,20], 10))
