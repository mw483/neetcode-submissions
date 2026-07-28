from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        
        # Only create bucket lists for frequencies that actually occur
        buckets = defaultdict(list)
        for num, count in counts.items():
            buckets[count].append(num)
        
        res = []
        # Walk down from the maximum possible frequency
        for freq in range(len(nums), 0, -1):
            if freq in buckets:
                res.extend(buckets[freq])
                if len(res) >= k:
                    return res[:k]
        return res