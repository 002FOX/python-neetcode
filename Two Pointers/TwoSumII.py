# Binary search can also work, two pointers is O(n)
def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        left = 0
        right = len(numbers) - 1

        if len(numbers) == 2:
            return [1,2]
    
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            if numbers[left] + numbers[right] > target:
                right -= 1
            if numbers[left] + numbers[right] < target:
                left += 1
        return []
