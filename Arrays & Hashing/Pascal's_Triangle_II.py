# Link: https://leetcode.com/problems/pascals-triangle-ii/

def getRow(rowIndex):
    res = [1]

    for i in range(rowIndex):
        nextRow = [0] * (len(res) + 1)
        for j in range(len(res)):
            nextRow[j] += res[j]
            nextRow[j+1] += res[j]
        res = nextRow
    return res
print(getRow(4))