class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two pointers in sorted array
        nums.sort()
        results = []
        for i, a in enumerate(nums):
            if a > 0:
                break # All remaining numbers are positive, cannot add up to 0
            if i > 0 and a == nums[i - 1]:
                continue # Skip duplicates
            # Pointer 1 starts just after i
            l = i + 1
            # Pointer 2 starts at the end
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # Add triplet to result
                    results.append([a, nums[l], nums[r]])
                    # Move both pointers inward
                    l += 1
                    r -= 1
                    # Skip duplicates at the left pointer
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return results

