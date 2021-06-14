class Solution:
    def reverse(self, x: int) -> int:        
        pointer = 0
        for initialVal in nums:
            if initialVal != val:
                nums[pointer] = initialVal
                pointer += 1
        return pointer
        '''
        # alternative: cheating
        while val in nums:
            nums.remove(val)
        return len(nums)

        # alternative: 2 pointers
        initial = 0
        pointer = len(nums) - 1
        while initial <= pointer:
            if nums[initial] == val:
                nums[initial] = nums[pointer]
                pointer -= 1
            else:
                initial += 1
        return initial
        '''