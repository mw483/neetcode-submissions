class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numSet = set(nums)
        lenNums = len(nums)
        for n in numSet:
            count = 0
            for m in nums:
                if m == n: 
                    count += 1
                if count == (lenNums // 2 + 1):
                    return n