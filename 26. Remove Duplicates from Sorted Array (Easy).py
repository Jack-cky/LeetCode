class Solution:
    def reverse(self, x: int) -> int:        
        nums[:] = sorted(set(nums))
        return len(nums)
        '''
        # alternative
        initial = 0
        pointer = 1
        while initial != len(nums):
            if len(nums) in [pointer, initial]:
                break
            if nums[initial] == nums[pointer]:
                pointer += 1
                continue
            initial += 1
            nums[initial] = nums[pointer]
            pointer += 1
        return initial + 1
        '''