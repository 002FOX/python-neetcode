# Words can have any character so we simply put a delimiter ! as well as the length of the word inbetween each word to easily decode it.
def encode(self, strs):
    result = ''
    for s in strs:
        result += str(len(s)) + '!' + s
    return result

def decode(self, s):
    result = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != '!':
            j += 1
        length = int(s[i:j])
        result.append(s[j + 1:j + 1 + length])
        i = j + 1 + length
    return result
