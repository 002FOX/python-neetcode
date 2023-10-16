# Makes a set, checks if the number is in the set in average O(1), if not add to the set.
# Space: O(n) 
# Time: O(n)
def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for x in nums:
            if x in s:
                return True
            s.add(x)
        return False