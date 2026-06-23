class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Get two bars that maximize height
        # Get two bars separated the farthest -> Get index
        # If you pick a pair, the height will be the min of the pair
        if len(set(heights)) == 1:
            return heights[0] * (len(heights) - 1)

        # initialize area
        area = 0

        # while i < j
        # area = min([heights[i], heights[j]]) * (j - i) 
        i = 0
        j = len(heights) - 1

        while i < j:
            # Skip if height = 0 since unusable
            if heights[i] == 0:
                i += 1
                continue
            if heights[j] == 0:
                j -= 1
                continue
            area = max(area, min([heights[i], heights[j]]) * (j - i)) 
            # Only move the pointer that has the smaller value
            # Because to get the largest area
            # We have to increase the minimum
            if heights[i] < heights[j]:
                i += 1
                continue
            if heights[j] <= heights[i]:
                j -= 1
                continue
            # Max area for a choice of bar is limited by
            # the number of remaining elements in the array

        return area
