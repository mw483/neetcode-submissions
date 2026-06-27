class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndexes = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numIndexes:
                return [numIndexes[diff], i]
            numIndexes[nums[i]] = i

