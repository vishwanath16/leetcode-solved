# Link: https://neetcode.io/problems/string-encode-and-decode

def encode(strs):
    """
    Encodes a list of strings to a single string.
    """
    encoded = ''

    for string in strs:
        encoded += str(len(string)) + '#' + string

    return encoded


def decode(s):
    """
    Decodes a single string back to a list of strings.
    """
    decoded = []
    i = 0

    while i < len(s):
        j = s.find('#', i)
        length = int(s[i:j])
        i = j + 1
        decoded.append(s[i:i + length])
        i += length

    return decoded


# Example 1
input1 = ["neet", "code", "love", "you"]
encoded1 = encode(input1)
decoded1 = decode(encoded1)
print("Encoded:", encoded1)
print("Decoded:", decoded1)
