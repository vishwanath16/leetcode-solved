# Link: https://leetcode.com/problems/guess-number-higher-or-lower/

def guessNumber(n):
    low, high = 1, n
    
    while low <= high:
        mid = (low + high) // 2
        result = guess(mid)
        
        if result == 0:
            return mid
        elif result == -1:
            high = mid - 1
        else:
            low = mid + 1