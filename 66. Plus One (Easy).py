class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        n = len(digits)
        for i in range(len(digits)):
            sum += digits[i] * 10 ** (n - 1 - i)
        sum += 1
        sum = str(sum)
        result = []
        for i in range(len(sum)):
            result.append(sum[i])
        return result