class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # example : nums=[1,2,1,0,4,2,6], k=3
        from collections import deque
        output = []
        q = deque() # deque stores indexes

        # len(nums) = 7
        

        l = r = 0
        # expand via the right pointer
        while r < len(nums):
            # before inserting the new index, remove indices with values smaller than the new value
            # "while q" -> while the deque has an element.
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # add the new index to the queue
            q.append(r)

            # if the left pointer passes the front index, 
            # remove using popleft, as it is out of the window
            if l > q[0]:
                q.popleft()

            # once the window reaches size k, time to get the output
            if (r + 1) >= k: # this if condition only runs after the first k elements are appended.
                output.append(nums[q[0]])
                # after updating, move the left pointer.  
                l += 1
            # move the right pointer to complete the window slide.
            r += 1
        
        return output

# iteration 1 : q = [0]
# 2 : 


            