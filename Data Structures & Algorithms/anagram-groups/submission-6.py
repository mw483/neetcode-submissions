class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in range(len(strs)):
            char_counts = [0] * 26
            for char in strs[i]:
                char_counts[ord(char) - ord('a')] += 1
            groups[tuple(char_counts)].append(strs[i])
        return list(groups.values())
