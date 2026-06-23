class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force
        # Edge case: zeros
        output = []
        nums_copy = nums
        for i, n in enumerate(nums):
            res = 1
            for j, m in enumerate(nums_copy):
                if j != i:
                    res *= m
            output.append(res)
        return output 

