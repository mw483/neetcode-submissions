class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # From brute force method we learn that: 
        # We need to multiply those without matching index
        # For O(n) solution we need to get result while traversing only once
        # Brute force 2
        output = [1] * len(nums)
        for i, n in enumerate(output):
            for j, m in enumerate(nums):
                if i != j:
                    output[i] *= m
        return output 

