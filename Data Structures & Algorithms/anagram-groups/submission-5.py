class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        groups = defaultdict(list)
        # loop through strings
        for s in strs:
            freq = [0] * 26
            # loop through each character to build the frequency array
            for c in s:
                freq[ord(c) - ord('a')] += 1
            # add the frequency array as the key, append the string
            groups[tuple(freq)].append(s)
        return list(groups.values())
            