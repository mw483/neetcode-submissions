class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if all elements are unique, then in the original array,
        # the minimum is in index 0. But after rotation it will be
        # located in index 0 + (#of rotation)%len(n).
        # find minimum of each segment
        # to find where the segment is, find the # of rotation
        # we know that nums[0] is the smallest of the first segment
        # we know that nums[n - 1] is the largest of the second segment.
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return res