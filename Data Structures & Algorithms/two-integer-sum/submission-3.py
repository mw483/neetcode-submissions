class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in numSet:
                numSet[nums[i]] = i
            else:
                return [numSet[diff], i]