class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialize array to count occurrences
        count = {}
        # array to store buckets, freq[i] will store numbers that appear i times as a list
        freq = [[] for i in range(len(nums) + 1)]
        #count occurrences
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # append occurrences to the buckets
        for n, c in count.items():
            freq[c].append(n)

        #initialize empty result array
        res = []

        # loop through the buckets
        for i in range(len(freq) - 1, 0, -1):
            # loop through each bucket
            for n in freq[i]:
                # add the number to the result
                res.append(n)
                # return if we appended enough elements as requested in k
                if len(res) == k:
                    return res

        