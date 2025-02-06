# Link: https://leetcode.com/problems/number-complement/description/

def findComplement(num):
    bit_length = num.bit_length()
    
    mask = (1 << bit_length) - 1
    
    return num ^ mask

print(findComplement(5))
        

