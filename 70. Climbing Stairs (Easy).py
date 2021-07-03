class Solution:
    def climbStairs(self, n: int) -> int:
        current = previous = 1
        for i in range(n):
            current, previous = previous, current + previous
        return current