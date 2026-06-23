class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Use prefix and suffix array
        # res[i] = pref[i] * suff[i]
        len_nums = len(nums)
        res = [0] * len_nums
        pref = [0] * len_nums
        suff = [0] * len_nums
        pref[0] = 1 # Nothing to the left of index 0
        suff[len_nums-1] = 1 # Nothing to the right of last index
        # Build the prefix product array
        for i in range(1, len_nums):
            pref[i] = nums[i-1] * pref[i-1]
        # Build the suffix product array
        for i in range(len_nums-2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]
        for i in range(len_nums):
            res[i] = pref[i] * suff[i]
        return res

            
