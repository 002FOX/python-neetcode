# Constraints: We want O(n) runtime and we cannot use division, and we want O(1) space.
# We pass through the array to calculate the prefixes and then with the help of a temporary variable we modify the output array to get the product
# Time : O(n) we pass through the array twice
# Space : O(1) we only make the postfix variable.
def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        output.append(1)

        for i in range(1, len(nums)):
            output.append(output[i-1]*nums[i-1])

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output