class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        
        # loop through each element in sorted array
        for i, a in enumerate(sorted_nums):
            # if the smallest number in the array is >= zero, 
            # then all the other elements are positive
            # and cannot sum to zero
            if a > 0:
                break
        
            # for each element, run a two pointer search
            # on the rest of the elemennts
            if i > 0 and a == sorted_nums[i - 1]:
                continue
            l = i + 1
            r = len(sorted_nums) - 1
            while l < r:
                three_sum = a + sorted_nums[l] + sorted_nums[r] 
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([a, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    while sorted_nums[l] == sorted_nums[l - 1] and l < r:
                        l += 1
        return res

