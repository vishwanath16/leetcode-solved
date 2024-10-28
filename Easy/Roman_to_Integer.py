# Link: https://leetcode.com/problems/roman-to-integer/description/

def romanToInt(s):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    total = 0

    for i in range(len(s)):
        if dic[s[i]] < dic[s[i + 1]]:
            total -= dic[s[i]]
        else:
            total += dic[s[i]]

    total += dic[s[-1]]
    
    return total

print(romanToInt("MCMXCIV"))  # Output should be 1994
