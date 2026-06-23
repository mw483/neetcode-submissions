class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        prefix_max = [0] * n
        suffix_max = [0] * n

        # build prefix and suffix arrays
        prefix_max[0] = height[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], height[i])
        
        suffix_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i])

        total = 0
        # Calculate total water
        for i in range(n):
            total += min(prefix_max[i], suffix_max[i]) - height[i] 
        
        return total