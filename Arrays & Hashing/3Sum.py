# Link: https://leetcode.com/problems/3sum/

def threeSum(nums):
    res = []
    nums.sort()  

    for i, a in enumerate(nums):  
        if a > 0:
            break  
        if i > 0 and a == nums[i - 1]:
            continue  

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1  
            elif threeSum < 0:
                l += 1  
            else:
                res.append([a, nums[l], nums[r]])  
                l += 1
                r -= 1
                
                while l < r and nums[l] == nums[l - 1]:
                    l += 1


    return res


print(threeSum([-4, -1, -1, -1, 0, 1, 2, 2]))