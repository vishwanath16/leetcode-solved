# Link: https://leetcode.com/problems/license-key-formatting/

def licenseKeyFormatting(s, k):
    s = s.replace('-', '').upper()
    n = len(s)
    first_group_size = n % k if n % k != 0 else k
    result = s[:first_group_size]
    for i in range(first_group_size, n, k):
        result += '-' + s[i:i+k]
    return result


print(licenseKeyFormatting("2-5g-3-J", 2))