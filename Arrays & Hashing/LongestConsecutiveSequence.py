# O(n) : No sorting, using a set with O(1) Lookups, find the first element of a sequence that has no left neighbour and then count the length of its sequence.
def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0
    new_set = set(nums)
    output = 1

    for x in new_set:
        if x-1 not in new_set:
            curr_streak = 1
            temp = x
            while True:
                if temp+1 in new_set:
                    curr_streak += 1
                    temp+= 1
                else:
                    break
            output = max(output, curr_streak)

    return output

# Cleaner code
def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        new_set = set(nums)
        output = 1

        for x in new_set:
            if x-1 not in new_set:
                curr_streak = 1
                while x+curr_streak in new_set:
                    curr_streak += 1
                output = max(output, curr_streak)

        return output
