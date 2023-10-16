# We store the numbers in hashmap while we check if the target minus the current value in array exists already, if so we found both.
# Time : O(n) One Pass
# Space : O(n) We make a hashmap

def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            c = target - value
            if c in hashmap:
                return [hashmap[c], index]
            hashmap[value] = index
        return []