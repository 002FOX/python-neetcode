# Hint: at i the equation is min(maximumLeftHeight, maximumRightHeight) - height[i]. Using two pointers left and right we dont need to find out the min of both left and right of i, only the current pointer we shifted. Thi is because the max left or right
will be smaller than whatever is on the opposite side.
def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        rainTrapped = 0
        while left < right:
            if maxLeft <= maxRight:
                left +=1
                if maxLeft - height[left] > 0:
                    rainTrapped += maxLeft - height[left]
                maxLeft = max(maxLeft, height[left])
            else:    
                right -=1
                if maxRight - height[right] > 0:
                    rainTrapped += maxRight - height[right]
                maxRight = max(maxRight, height[right])
        return rainTrapped
