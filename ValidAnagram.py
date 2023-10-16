# We make an array for the alphabet (assuming every char is lowercase) if both words are anagrams the index of the char will increment and decrement
# back to 0
# Time : O(n) We iterate through both strings
# Space : O(1) We make an array of 26 

def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        alphabet = [0] * 26
        for c1, c2 in zip(s, t):
            alphabet[ord(c1) - ord('a')]+= 1
            alphabet[ord(c2) - ord('a')]-= 1
        
        return all(x == 0 for x in alphabet)