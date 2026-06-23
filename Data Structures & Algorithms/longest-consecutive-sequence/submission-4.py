class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 # initialize count
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        for n in nums:
            if (n - 1) not in nums_set:
                length = 0
                while (n + length) in nums_set:
                    length += 1
                longest = max(length, longest)
        return longest

        



        