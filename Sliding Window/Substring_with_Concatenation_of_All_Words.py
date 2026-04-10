# Link: https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from collections import Counter


def findSubstring(s, words):
    if not s or not words: return []
    
    word_len = len(words[0])
    num_words = len(words)
    window_len = word_len * num_words
    word_freq = Counter(words)
    result = []

    for i in range(len(s) - window_len + 1):
        seen = {}
        j = 0
        while j < num_words:
            word = s[i + j * word_len : i + (j + 1) * word_len]
            if word not in word_freq:
                break
            seen[word] = seen.get(word, 0) + 1
            if seen[word] > word_freq[word]:
                break
            j += 1
        if j == num_words:
            result.append(i)
    return result

print(findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))