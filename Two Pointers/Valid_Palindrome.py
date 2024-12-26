# Link: https://leetcode.com/problems/valid-palindrome/description/

import re

def isPalindrome(s):
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        return True if cleaned_text[::-1] == cleaned_text else False

print(isPalindrome('wow'))