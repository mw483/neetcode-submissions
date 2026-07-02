class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # remember that we have the array in two sorted parts
        # in the example of [3,4,5,6,1,2], target=1
        # mid = (0 + 5) // 2 = 2
        # nums[2] = 5

        # first, find the pivot

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l
        # reset the pointers, now only searching the wanted segment
        l, r = 0, len(nums) - 1

        # if the target is larger than the pivot point and smaller than nums[r], 
        # search right half by setting left pointer to the pivot
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        # else search the left half
        else:
            r = pivot - 1

        # run another binary search
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

