class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for n in nums:
            frequencies[n] = frequencies.get(n, 0) + 1
        sorted_list = sorted(frequencies, key=frequencies.get, reverse=True)
        return sorted_list[:k]