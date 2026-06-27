class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        # use defaultdict
        groups = defaultdict(list)
        for s in strs:
            # check the character frequency of the current string
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            # append the current string to the group with the frequency as the key
            groups[tuple(freq)].append(s)
        return list(groups.values()) 


