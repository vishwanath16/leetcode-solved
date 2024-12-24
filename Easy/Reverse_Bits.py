# https://leetcode.com/problems/reverse-bits/description/

def reverseBits(n):
    return int(f'{n:032b}'[::-1], 2)

print(reverseBits(0b00000010100101000001111010011100))