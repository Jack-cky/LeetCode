class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = n = len(nums)
        while right >= left:
            middle = (left + right) // 2
            if middle >= n:
                break
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return left
        '''
        # alternative: cheating
        from bisect import bisect_left
        bisect_left(nums, target)

        # alternative: cheating
        sorted(nums + [target]).index(target)
        '''