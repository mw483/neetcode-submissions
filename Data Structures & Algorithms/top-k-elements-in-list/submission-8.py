from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # buckets of frequencies
        buckets = [[] for _ in range(len(nums) + 1)] # buckets from 0 to len(nums)
        counts = Counter(nums) # count the occurrences of each number
        for num, count in counts.items():
            buckets[count].append(num)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
