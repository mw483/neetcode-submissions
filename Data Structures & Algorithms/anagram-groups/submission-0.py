class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = [] # A list of anagram groups
        anagrams = [] # Grouped anagrams - nested lists
        # Lists starts empty
        # Build the anagram groups
        for str in strs:
            # Count each word. 
            counts = {}
            for i in range(len(str)):
                counts[str[i]] = counts.get(str[i], 0) + 1 
            if counts not in anagram_groups:
                # If does not exist yet, add the counts into the list of anagram groups
                anagram_groups.append(counts)
                anagrams.append([]) # and create empty list per group
        for str in strs:
            counts = {}
            for i in range(len(str)):
                counts[str[i]] = counts.get(str[i], 0) + 1
            for i in range(len(anagram_groups)):
                if counts ==  anagram_groups[i]:
                    anagrams[i].append(str)
        return anagrams

             