class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        aggSum = minSum = 0
        result = float('-inf')
        for val in nums:
            aggSum += val
            if(aggSum - minSum) > result:
                result = aggSum - minSum
            if aggSum < minSum:
                minSum = aggSum
        return result