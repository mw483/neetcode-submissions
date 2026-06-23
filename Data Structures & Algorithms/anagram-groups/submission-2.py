class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            # initialize frequency array
            freq = [0] * 26
            # count frequency of each letter in each string
            for c in s:
                freq[ord(c) - ord('a')] += 1
            # add the array as a key for the result array with the string as the key
            res[tuple(freq)].append(s)
        return list(res.values())

        