class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialize counter for each number
        count = {}
        # initialize frequency buckets,  0 to len(nums)
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            # count the nums
            count[n] = 1 + count.get(n, 0)
        # insert into buckets
        for n, cnt in count.items():
            freq[cnt].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                

