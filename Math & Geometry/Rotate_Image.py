# Link: https://leetcode.com/problems/rotate-image/description/

def rotate(matrix):
    left , right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            #save the topleft
            topLeft = matrix[top][left + i]

            # move bottom left into top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # move bottom right into bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # move top right into bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # move top Left into top right
            matrix[top + i][right] = topLeft

        left += 1
        right -= 1

    return matrix

print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))