class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # initialize the buckets
        # For example freqBuckets[i] contains a list of elements with frequency i 
        freqBuckets = [[] for i in range(len(nums) + 1)]

        # Loop through the array and count the occurence of each number
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # Insert into the buckets
        for num, freq in counts.items():
            freqBuckets[freq].append(num)
        
        # Loop through the buckets to get the output array
        res = []
        for i in range(len(freqBuckets) - 1, 0, -1):
            for num in freqBuckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

