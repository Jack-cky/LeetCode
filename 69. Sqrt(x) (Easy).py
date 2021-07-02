class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            middle = left + (right - left) // 2
            if (middle * middle <= x) and ((middle + 1) * (middle + 1) > x):
                return middle
            elif x < middle * middle:
                right = middle - 1
            else:
                left = middle + 1