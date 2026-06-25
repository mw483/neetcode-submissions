class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Use deque
        from collections import deque
        output = []

        # initialize empty window as a deque
        window = deque()

        # loop through array
        l = 0
        # use fixed size sliding window of size k
        for r in range(len(nums)):
            # append to the fixed size sliding window when the 
            # window is still smaller than requested
            window.append(nums[r])

            # start calculating the max and append-remove, 
            # and slide the left pointer
            # only if the window if the valid size
            if len(window) == k:
                output.append(max(window))
                window.popleft()
                l += 1

        return output