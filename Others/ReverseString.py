# string.reverse()

def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = (len(s) // 2)
        for i in range(length):
            temp = s[i]
            s[i] = s[len(s)- 1 - i]
            s[len(s) - i - 1] = temp

# OR

def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1