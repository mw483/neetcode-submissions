class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            char_counts = [0] * 26
            for char in s:
                char_counts[ord(char) - ord('a')] += 1
            groups[tuple(char_counts)].append(s)
        return list(groups.values())
