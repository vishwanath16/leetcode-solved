# Link: https://leetcode.com/problems/excel-sheet-column-title/

def convertToTitle(columnNumber):
    res = ''
    while columnNumber > 0:
        rem = (columnNumber - 1) % 26
        res += chr(ord('A') + rem )
        columnNumber = (columnNumber - 1) // 26

    return res[::-1]


print(convertToTitle(8853))