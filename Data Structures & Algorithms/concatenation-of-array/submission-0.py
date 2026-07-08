class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = nums.copy()
        for num in nums:
            output.append(num)
        return output