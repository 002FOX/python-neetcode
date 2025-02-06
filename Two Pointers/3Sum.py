# Sorting to make dups easier, then for each number using two pointers we look for the triplet. For the first element we only start if its the last duplicate, then when we find the other 2 we skip to their last dupes respectively as well
def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
