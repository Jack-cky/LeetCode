class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i, value in enumerate(nums):
            if target - value in hashTable:
                return hashTable[target - value], i
            hashTable[value] = i