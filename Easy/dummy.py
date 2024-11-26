def mergeAlternately(word1, word2):
    result = ''
    for i, j in zip(word1, word2):
        result += i + j

    result += word2[len(word1):]

    

    return result


print(mergeAlternately("hello", "worldSheep"))