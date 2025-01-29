# Link: https://leetcode.com/problems/product-of-array-except-self/description/

# Brute Force Solution

# def productExceptSelf(nums):
#     result = []

#     for i in range(len(nums)):
#         product = 1
#         for j in range(len(nums)):
#             if i != j:
#                 product *= nums[j]
        
#         result.append(product)

#     return result

# print(productExceptSelf([-1,1,0,-3,3]))


# Linear Time Solution

def productExceptSelf(nums):
    res = [1] * len(nums)

    prefix = 1

    for i in range(len(nums)):
        res[i] = prefix 
        prefix *= nums[i]

    postfix = 1

    for i in range(len(nums) -1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


print(productExceptSelf([1,2,3,4]))