class Solution:
  # Iterative way, my favorite
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        while start <= end:
            if target > nums[mid]:
                start = mid + 1
                mid = (start + end) // 2
            elif target < nums[mid]:
                end = mid-1
                mid = (start + end) // 2
            elif target == nums[mid]:
                return mid
        return -1

    # Recursive
    def bs(self, nums: List[int], start: int, end: int, target: int):
          if start > end:
              return -1
          mid = (start + end) // 2
          if nums[mid] > target:
              return self.bs(nums, start, mid -1, target)
          elif nums[mid] < target:
              return self.bs(nums, mid+1, end, target)
          elif nums[mid] == target:
              return mid
  
      def search(self, nums: List[int], target: int) -> int:
          return self.bs(nums, 0, len(nums) - 1, target)
