# Hashmap with the key being a tuple (immutable) of the character count of the string and the value is a list of the anagrams/
# Time: O(n*k) k is average size of string
# Space: O(n*k) hashmap is dominant 
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for string in strs:
            alphabetCount = [0] * 26

            for ch in string:
                alphabetCount[ord(ch) - ord('a')]+= 1
                
            key = tuple(alphabetCount)
            hashmap[key].append(string)

        return list(hashmap.values())
